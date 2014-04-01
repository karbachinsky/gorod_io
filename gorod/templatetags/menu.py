""" Menu template tags for gorod """ 

from django import template

from gorod.models import ArticleRubric

register = template.Library()

@register.filter(name='menu')
def menu(city, city_id):
    """ Display memu for city """
    article_rubrics = ArticleRubric.objects.all

    menu = [city, article_rubrics]

    return menu


    


