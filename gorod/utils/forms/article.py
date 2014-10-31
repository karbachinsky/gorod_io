# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea, TextInput, ClearableFileInput
#from captcha.fields import CaptchaField

from django.forms import ModelForm, Textarea, TextInput, HiddenInput, BooleanField
from gorod.models import Article, ArticleRubric


class ArticleAddForm(ModelForm):
    """
        Article add form
    """
    def __init__(self, *args,**kwargs):
        super(ArticleAddForm, self).__init__(*args, **kwargs)
        #assert False, repr(self.fields['city'])
        #self.fields['rubric'].queryset = ArticleRubric.objects.filter(city__id=2)

    class Meta:
        model = Article
        fields = ['picture', 'title', 'rubric', 'text', 'city']
        localized_fields = ['picture', 'title', 'rubric', 'text', 'city']
        widgets = {
            'text': Textarea(attrs={'placeholder': 'Введите текст'}),
            'title': TextInput(attrs={'placeholder': 'Введите заголовок','autocomplete':'off'}),
            'picture': ClearableFileInput(attrs={'placeholder': 'Изображение'}),
            'city': HiddenInput(),
        }

    def is_valid(self):
        if not super(ArticleAddForm, self).is_valid():
            return False

        if not self.cleaned_data['text'] and not self.cleaned_data['picture']:
            self._errors['internal'] = [u'Текст или изображение должно быть заполнено!']
            return False

        return True
