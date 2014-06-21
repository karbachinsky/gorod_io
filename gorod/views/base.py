from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db import IntegrityError, DatabaseError

from django.contrib.auth.decorators import login_required

from gorod.models import City, Article, ArticleRubric
from gorod.utils.forms.article import ArticleAddForm

#from django.core.urlresolvers import reverse


def index(request):
    """
        Gorod main page
    """
    cities = City.objects.order_by('title').all

    context = {
        'cities': cities
    }

    return render(request, 'gorod/index.html', context)


def feed(request, city_name='belev', rubric_name=None):
    """
        One city main page (feed)
    """
    city = get_object_or_404(City, name=city_name)

    filters = {
        'city': city.id,
        'is_published': True,
        'is_checked': True
    }

    rubric = None
    if rubric_name:
        rubric = get_object_or_404(ArticleRubric, name=rubric_name)
        filters['rubric'] = rubric.id 

    articles = Article.objects.filter(**filters)\
                              .order_by('-add_date')\
                              .select_related()

    context = {
        'articles': articles,
        'city': city,
        'rubric': rubric
    }

    return render(request, 'gorod/feed.html', context)


def article(request, city_name, article_id):
    """
        One article page
    """
    city = get_object_or_404(City, name=city_name)
    article_item = get_object_or_404(Article, pk=article_id, city=city.id)

    context = {
        'article': article_item,
        'city': city
    }

    return render(request, 'gorod/article.html', context)


@login_required
def add_article_form(request, city_name):
    """
        Add article page and form processor
    """
    city = get_object_or_404(City, name=city_name)

    # TODO: check is user trying to add article to his city
    form = None

    if request.method == 'POST':
        form = ArticleAddForm(request.POST)
        if form.is_valid():
            user_article = form.save(commit=False)

            user_article.city = city
            user_article.user = request.user
            # Article must be checked by admin if user is not admin
            if not request.user.has_perm('gorod.article_create_wo_check'):
                user_article.is_checked = False

            try:
                user_article.save()
            except (DatabaseError, IntegrityError) as e:
                raise e

            return render(request, 'gorod/forms/article_add_ok.html')
    else:
        form = ArticleAddForm()

    return render(request, 'gorod/forms/article_add.html', {
        'form': form,
    })


def handler404(request):
    return render(request, '404.html')


def handler500(request):
    return render(request, '500.html')


