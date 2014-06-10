from django.forms import ModelForm

from gorod.models import Article


class ArticleAddForm(ModelForm):
    """
        Article add form
    """
    class Meta:
        model = Article
        fields = ['picture', 'title', 'rubric', 'text']

