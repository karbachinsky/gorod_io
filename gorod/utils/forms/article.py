# -*- coding: utf-8 -*-

from django.forms import ModelForm
from captcha.fields import CaptchaField

from gorod.models import Article

class ArticleAddForm(ModelForm):
    """
        Article add form
    """
    #captcha = CaptchaField(label=u'Проверочный код:')

    class Meta:
        model = Article
        fields = ['picture', 'title', 'rubric', 'text']
        localized_fields = ['picture', 'title', 'rubric', 'text']

