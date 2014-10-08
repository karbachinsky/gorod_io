# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse, NoReverseMatch
from django.conf import settings
from django.core import serializers

from easy_thumbnails.templatetags.thumbnail import thumbnail_url
from ckeditor.fields import RichTextField

from gorod.models import City
from gorod.utils.exceptions import FeedError
from gorod.templatetags.stringutils import smart_truncate

from smart_selects.db_fields import ChainedForeignKey


class ArticleRubric(models.Model):
    """
        ArticleRubric class
    """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_plural = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = 'gorod'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self, city=None):
        try:
            return reverse('gorod:feed-rubric', kwargs={
                'city_name': city.name,
                'rubric_name': self.name
            })
        except NoReverseMatch:
            return '/'

    def natural_key(self):
        return {
            'name': self.name,
            'title': self.title
        }


class ArticleManager(models.Manager):
    """
        Queryset manager for Article model
    """
    def get_json_feed(self, filters, page=0, limit=15):
        """
            Article list in json format
        """

        if page < 0 or limit <= 0:
            raise FeedError('Bad page and limit parameters!')

        articles = self.model.objects.filter(**filters)\
                             .order_by('-add_date')\
                             .select_related()

        lim_start = page*limit
        lim_end = lim_start + limit

        total_cnt = articles.count()

        articles = articles.all()[lim_start:lim_end]

        for article in articles:
            article.rubric.url = article.rubric.get_absolute_url(article.city)

        # FIXME: add try-catch
        json_feed = serializers.serialize('json', articles,
            indent=4,
            extras=('url', 'thumbnail', 'short_text', 'human_add_date'),
            relations={
                'rubric': {
                    'extras': ('url',)
                },
                'user': {
                    'extras': ('profile_url', 'human_name', 'full_avatar'),
                    'fields': ('id',)
                }
            },
            excludes=('text', 'is_checked', 'is_published', 'add_date', 'city')
        )

        # FIXME! GOVNOKOD! Use django rest framework
        json_response = '{"total": %d, "feed": %s}' % (total_cnt, json_feed)

        return json_response

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
    rubric = models.ForeignKey(ArticleRubric, default=1, help_text=u'Рубрика')
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

