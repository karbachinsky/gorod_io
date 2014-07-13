# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea, TextInput, FileInput
#from captcha.fields import CaptchaField

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
        widgets = {
            'text': Textarea(attrs={'placeholder': 'Текст'}),
            'title': TextInput(attrs={'placeholder': 'Заголовок'}),
            'picture': FileInput(attrs={'placeholder': 'Изображение'}),
        }

