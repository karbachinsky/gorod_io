from django.shortcuts import render, get_object_or_404, Http404, HttpResponse
from django.db import IntegrityError, DatabaseError
from django.views.generic import View
from django.core import serializers

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import simplejson

from gorod.models import City, Article, ArticleRubric
from gorod.utils.forms.article import ArticleAddForm


class FeedView(View):
    """
        Show list of articles for the certain city and rubric.
    """
    def dispatch(self, request, city_name, rubric_name=None):
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
            'rubric': rubric
        }

        # FIXME
        if request.GET.get('json'):
            page = int(request.GET.get('page', 0))
            limit = int(request.GET.get('limit', 15))
            #assert False, "%s %s" % (page, limit)
            lim_start = page*limit
            lim_end = lim_start + limit
            json_data = serializers.serialize('json', articles.all()[lim_start:lim_end])
            return HttpResponse(json_data, mimetype='application/json')
        else:
            context['articles'] = context['articles'].all()[0:1000]
            return render(request, 'gorod/feed.html', context)


class ArticleView(View):
    """
        One article page.
    """
    def dispatch(self, request, city_name, article_id):
        article_item = get_object_or_404(Article, pk=int(article_id),\
                                                  city__name=city_name,\
                                                  is_published=True)

        if not article_item.is_checked:
            # If user is article author - he can see it anyway. Else - checking
            if article_item.user != request.user:
                # Checking if user can se not approved articles
                if not request.user.has_perm('gorod.article_see_not_checked'):
                    raise Http404
                    #pass

        context = {
            'article': article_item,
        }


        return render(request, 'gorod/article.html', context)


class AddView(View):
    """
        Add articles
    """

    @method_decorator(login_required)
    def dispatch(self, request, city_name):

        city = get_object_or_404(City, name=city_name)

        # TODO: check is user trying to add article to his city
        form = None

        if request.method == 'POST':
            form = ArticleAddForm(request.POST, request.FILES)
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