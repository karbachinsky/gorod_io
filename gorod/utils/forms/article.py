# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea, TextInput, FileInput
#from captcha.fields import CaptchaField

from django.forms import ModelForm, Textarea, TextInput, HiddenInput
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
            'title': TextInput(attrs={'placeholder': 'Заголовок','autocomplete':'off'}),
            'picture': FileInput(attrs={'placeholder': 'Изображение'}),
            'rubric': HiddenInput(),
        }

    def is_valid(self):
        if not super(ArticleAddForm, self).is_valid():
            return False

        if not self.cleaned_data['text'] and not self.cleaned_data['picture']:
            self._errors['internal'] = [u'Текст или изображение должно быть заполнено!']
            return False

        return True

