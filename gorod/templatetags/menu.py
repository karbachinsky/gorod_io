""" Menu template tags for gorod """ 

from django import template
from gorod.models import ArticleRubric
from django.core.urlresolvers import reverse


register = template.Library()


@register.inclusion_tag('gorod/templatetags/menu.html')
def menu(city):
    """ Display menu for city """

    # First element is city
    menu = [{
        'title': city.title,
        'link': reverse('gorod:city', kwargs={ 'city': city.name }),
        'is_active': 0
    }]

    # Than addding list of rubrics
    for rubric in list(ArticleRubric.objects.all()):
        menuitem = {
            'title': rubric.title,
            'link': reverse('gorod:feed_rubric', kwargs={ 
                'city': city.name, 
                'rubric_name': rubric.name
            }),
            'is_active': 0
        }

        menu.append(menuitem)

    # Adding organizations
    menu.append({
        'title': 'Organizations',
        'link': reverse('gorod:organizations', kwargs={'city': city.name}),
        'is_active': 0
    })

    return {'menu': menu}


