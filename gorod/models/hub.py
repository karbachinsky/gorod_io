# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.validators import MinLengthValidator


from gorod.models import City

from ckeditor.fields import RichTextField

from smart_selects.db_fields import ChainedForeignKey
from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager


class HubQuestionCategoryTreeManager(TreeManager):
    pass


class HubQuestionCategory(MPTTModel):
    """
        Hub question category tree
    """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_hubquestioncategory'
        verbose_name = 'city question category'
        verbose_name_plural = 'city question categories'

    tree = HubQuestionCategoryTreeManager()

    def __unicode__(self):
        return self.title


class HubQuestionManager(models.Manager):
    def get_questions_by_city_name(self, city_name):
        """
            List of questions corresponding to certain city
        """
        return self.model.objects.filter(city__name=city_name, is_published=True).select_related()

    def get_question_answers(self, question_id):
        """
            Get list of question answers by question_id
        """
        return HubAnswer.objects.filter(question__id=question_id, is_published=True)


class HubQuestion(models.Model):
    """
        city hub question
    """
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = TreeForeignKey(HubQuestionCategory, on_delete=models.PROTECT)
    question = models.CharField(max_length=500, validators=[MinLengthValidator(3)])
    description = RichTextField(max_length=3000, blank=True, null=True)
    picture = models.ImageField(max_length=255, upload_to='pictures/hub/%Y/%m/', null=True, blank=True, help_text=u'Изображение')
    user = ChainedForeignKey(
        settings.AUTH_USER_MODEL,
        chained_field="city",
        chained_model_field="city",
        show_all=False,
        auto_choose=True,
        on_delete=models.CASCADE
    )
    add_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_hubquestion'
        verbose_name = 'city question'
        verbose_name_plural = 'city questions'

    objects = HubQuestionManager()

    def get_absolute_url(self):
        return reverse('gorod:hub-question', kwargs={
            'city_name': self.city.name,
            'question_id': self.id
        })


class HubAnswer(models.Model):
    """
        city hub answer
    """
    question = models.ForeignKey(HubQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = RichTextField(max_length=3000, validators=[MinLengthValidator(3)])
    picture = models.ImageField(max_length=255, upload_to='pictures/hub/%Y/%m/', null=True, blank=True, help_text=u'Изображение')
    add_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_hubanswer'

    def get_absolute_url(self):
        # Temporary redirect to question
        return self.question.get_absolute_url()
