# -*- coding: utf-8 -*-

from django.db import models, DatabaseError, IntegrityError, transaction
from django.core.urlresolvers import reverse, NoReverseMatch
from django.conf import settings
from django.contrib.contenttypes.generic import GenericRelation
from django.utils.translation import ugettext as _
#from django.contrib.contenttypes.models import ContentType

from easy_thumbnails.templatetags.thumbnail import thumbnail_url
from ckeditor.fields import RichTextField

from gorod.models import City
from gorod.models.donc import DONC
from gorod.utils.exceptions import FeedError, DONCError
from gorod.templatetags.stringutils import smart_truncate
from gorod.utils.serializers.article import ArticleFeedSerializer

from comments import get_model as get_comments_model

from rest_framework.renderers import JSONRenderer

from smart_selects.db_fields import ChainedForeignKey

from likes.models import Like


class ArticleRubric(models.Model):
    """
        ArticleRubric class
    """
    FILTERS = (
        ('last',    _(u'Последние')),
        ('popular', _(u'Популярные')),
        #('hot', _(u'Горячие'))
    )

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    #title_plural = models.CharField(max_length=255, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(max_length=255,
                                upload_to='group_pictures/%Y/%m/',
                                null=True,
                                blank=True,
                                help_text=u'Изображение')
    description = models.TextField(null=True, blank=True, help_text=u'Описание')
    # #123245
    color = models.CharField(null=True, max_length=7)

    donc_data = GenericRelation(DONC, object_id_field='object_pk')

    class Meta:
        app_label = 'gorod'
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        unique_together = ('city', 'name')

    def __unicode__(self):
        return self.title

    @property
    def articles_cnt(self):
        """
            Number of articles
        """
        try:
            return self.donc_data.filter(field_name='articles_cnt')[0].count
        except IndexError:
            return 0

    @staticmethod
    def is_valid_filter(name):
        """
            Checks whether filter name is ok
        """
        for filter_name, filter_value in ArticleRubric.FILTERS:
            if filter_name == name:
                return True

        return False

    def get_absolute_url(self):
        try:
            return reverse('gorod:feed-rubric', kwargs={
                'city_name': self.city.name,
                'rubric_name': self.name
            })
        except NoReverseMatch:
            return '/'

    @property
    def url(self):
        return self.get_absolute_url()

    def natural_key(self):
        return {
            'name': self.name,
            'title': self.title
        }


class ArticleManager(models.Manager):
    """
        Queryset manager for Article model.
        articles is querySet
        Allows personalized feed
    """
    def construct_json_feed(self, articles, page=0, limit=15, user_id=None):
        """
            Article list in json format
        """

        if page < 0 or limit <= 0:
            raise FeedError('Bad page and limit parameters!')

        lim_start = page*limit
        lim_end = lim_start + limit

        total_cnt = articles.count()

        articles = articles.all()[lim_start:lim_end]

        serializer = ArticleFeedSerializer(articles, many=True)

        json_response = '{"total": %d, "feed": %s}' % (total_cnt, JSONRenderer().render(serializer.data))

        return json_response

    def get_by_group_filter(self, filter_name):
        """
            Select with respect to group filter
        """
        if 'last' == filter_name:
            return Article.objects.order_by('-add_date')
        elif 'popular' == filter_name:
            return Article.objects.order_by('-raiting')
        elif 'hot' == filter_name:
            return Article.objects.exclude(raiting=0).order_by('raiting')

        return Article.objects

    def get_all_published(self):
        return self.model.objects.filter(is_published=True).all()


class Article(models.Model):
    """
        Article class
    """
    # Size of truncated text preview in article list
    _SHORT_TEXT_LENGTH = 120

    title = models.CharField(max_length=255, help_text=u'Заголовок')
    add_date = models.DateTimeField(editable=False, auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    #rubric = models.ForeignKey(ArticleRubric, default=1, help_text=u'Рубрика')
    rubric = ChainedForeignKey(
        ArticleRubric,
        chained_field="city",
        chained_model_field="city",
        show_all=False,
        auto_choose=True
    )
    user = ChainedForeignKey(
        settings.AUTH_USER_MODEL,
        chained_field="city",
        chained_model_field="city",
        show_all=False,
        auto_choose=True
    )
    picture = models.ImageField(max_length=255, upload_to='pictures/%Y/%m/', null=True, blank=True, help_text=u'Изображение')
    text = RichTextField(blank=True, help_text=u'Текст')
    short_text = RichTextField(blank=True, null=True, help_text="Short text")
    is_published = models.BooleanField(default=True)
    is_checked = models.BooleanField(default=True)

    donc_data = GenericRelation(DONC, object_id_field='object_pk')

    comments = GenericRelation(get_comments_model(), object_id_field='object_pk')

    # Denormalaized value, special for fast selects
    raiting = models.IntegerField(default=0)

    objects = ArticleManager()

    class Meta:
        app_label = 'gorod'
        permissions = (
            ("article_create_wo_check", "Can create article without admin checking"),
            ("article_see_not_checked", "Can sen not approved articles"),
        )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        """
            Http Link to this article object
        """
        return reverse('gorod:article', kwargs={
            'city_name': self.city.name,
            'rubric_name': self.rubric.name,
            'article_id': self.id
        })

    url = property(get_absolute_url)

    @transaction.atomic
    def add_comment_hook(self, comment):
        """
            Called when someone adds comment to this article
        """
        from gorod.utils.donc import ArticleCommentsCounter

        article_comment_counter = ArticleCommentsCounter()

        try:
            article_comment_counter.set_object_cnt(self.id, self.comment_cnt + 1)
        except DONCError:
            pass

        # Adding notification
        self.user.add_notification(
            target=self,
            action='add-comment',
            target_user=comment.user
        )

    @transaction.atomic
    def add_like_hook(self, like):
        """
            Called when someone likes this article
        """
        from gorod.utils.donc import ArticlePositiveLikesCounter, ArticleNegativeLikesCounter

        if like.is_positive:
            article_likes_counter = ArticlePositiveLikesCounter()
        else:
            article_likes_counter = ArticleNegativeLikesCounter()

        try:
            article_likes_counter.set_object_cnt(self.id, self.likes_cnt(is_positive=like.is_positive) + 1)
            self.raiting = self.likes_cnt(is_positive=True) - self.likes_cnt(is_positive=False)
            self.save()
        except (DONCError, DatabaseError, IntegrityError):
            # Ok, we can miss it
            pass

        # Adding notification
        self.user.add_notification(
            target=self,
            action='add-like',
            target_user=like.user
        )

    @property
    def comment_cnt(self):
        """
            Number of comments
        """
        try:
            return self.donc_data.filter(field_name='comment_cnt')[0].count
        except IndexError:
            return 0

    def likes_cnt(self, is_positive=True):
        """
            Number of positive and negative likes
        """
        field_name = 'positive_likes_cnt' if is_positive else 'negative_likes_cnt'
        try:
            return self.donc_data.filter(field_name=field_name)[0].count
        except IndexError:
            return 0

    def is_already_liked_by_user(self, user):
        """
            Check whether user has already liked this
        """
        return Like.objects.has_user_liked_material(user, self)

    @property
    def thumbnail(self):
        """
            Picture thumbnail url
        """
        if self.picture:
            return thumbnail_url(self.picture, 'feed_image')
        else:
            return None

    def save(self, *args, **kwargs):
        self._set_short_text()
        super(Article, self).save(*args, **kwargs)

    def _set_short_text(self):
        """
            Sets short text (brief) for article preview
        """
        self.short_text = smart_truncate(self.text, self._SHORT_TEXT_LENGTH)

    @property
    def human_add_date(self):
        """
            Add date in human readable format
        """
        from django.contrib.humanize.templatetags.humanize import naturalday
        return naturalday(self.add_date)

    def can_user_modify(self, user):
        """
            Check if user can edit/delete current article object
        """
        return user.is_superuser or self.user == user


