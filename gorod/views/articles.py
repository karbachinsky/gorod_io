# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.db import IntegrityError, DatabaseError
from django.views.generic import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse

from gorod.models import City, Article, ArticleRubric
from gorod.utils.forms.article import ArticleAddForm
from gorod.utils.exceptions import FeedError

import json


class FeedView(View):
    """
        Show list of articles for the certain city and rubric.
    """
    def dispatch(self, request, city_name, rubric_name=None, filter_name='last'):
        city = get_object_or_404(City, name=city_name)
        rubric = None
        if rubric_name:
            rubric = get_object_or_404(ArticleRubric.objects.select_related('donc_data', 'city'),
                                       name=rubric_name,
                                       city__name=city_name)

        context = {
            'rubric': rubric,
            'group_filter': filter_name,
        }

        if request.user.is_authenticated():
            add_form = ArticleAddForm()
            add_form.patch_rubrics_qs(city)
            context['add_form'] = add_form

        return render(request, 'gorod/feed.html', context)


class GroupsView(View):
    """
        Show list of articles for the certain city and rubric.
    """
    def dispatch(self, request, city_name, rubric_name=None, filter_name='last'):
        rubric = None
        if rubric_name:
            rubric = get_object_or_404(ArticleRubric.objects.select_related('donc_data'),
                                       name=rubric_name,
                                       city__name=city_name)

        context = {
            'rubric': rubric,
            'group_filter': filter_name,
        }

        return render(request, 'gorod/groups.html', context)


class ArticleView(View):
    """
        One article page.
    """
    def dispatch(self, request, city_name, rubric_name, article_id):
        article = get_object_or_404(
            Article.objects.select_related(),
            pk=int(article_id),
            is_published=True
        )

        # If bad city or bad rubric was specified for article, then redirect to right url
        if article.city.name != city_name or article.rubric.name != rubric_name:
            return HttpResponsePermanentRedirect(article.url)

        if not article.is_checked:
            # If user is article author - he can see it anyway. Else - checking
            if article.user != request.user:
                # Checking if user can se not approved articles
                if not request.user.has_perm('gorod.article_see_not_checked'):
                    raise Http404
                    #pass

        context = {
            'article': article,
        }

        return render(request, 'gorod/article.html', context)


class ArticleAddView(View):
    """
        Add articles
    """
    def __init__(self):
        super(ArticleAddView, self).__init__()
        self.city = None
        self.rubric = None
        self.request = None

    @method_decorator(login_required)
    def dispatch(self, request, city_name):
        self.city = get_object_or_404(City, name=city_name)
        self.request = request

        # TODO: check is user trying to add article to his city
        if request.method == 'POST':
            instance = self.article if hasattr(self, 'article') and self.article is not None else None
            if instance or request.user.can_action('add-article'):
                form = ArticleAddForm(request.POST, request.FILES, instance=instance)
                json_response = self._save_form(form)
            else:
                json_response = dict(success=False, errors=[['time', [
                    u'Вы не можете добавлять новые материалы так часто! Попробуйте позже.']]])

            return HttpResponse(json.dumps(json_response), content_type='application/json')
        else:
            # Show form
            return self._display_form()

    def _display_form(self):
        form = ArticleAddForm()
        form.patch_rubrics_qs(self.city)

        return render(self.request, 'gorod/forms/article_add.html', {
            'form': form,
        })

    def _save_form(self, form):
        user = self.request.user
        if form.is_valid():
            user_article = form.save(commit=False)
            user_article.city = self.city
            user_article.user = user
            # Article must be checked by admin if user is not admin
            #if not request.user.has_perm('gorod.article_create_wo_check'):
            #    user_article.is_checked = False
            try:
                user_article.save()
            except (DatabaseError, IntegrityError) as e:
                raise e

            if not hasattr(self, 'article') and not user.is_superuser:
                user.make_action('add-article')
            response = dict(success=True, article_url=user_article.get_absolute_url())
        else:
            response = dict(success=False, errors=form.errors.items())

        return response


class ArticleEditView(ArticleAddView):
    """
        Edit user article
    """
    def __init__(self):
        super(ArticleAddView, self).__init__()
        self.article = None

    @method_decorator(login_required)
    def dispatch(self, request, city_name, rubric_name, article_id):
        self.article = get_object_or_404(Article, id=article_id, city__name=city_name, rubric__name=rubric_name)
        if not self.article.can_user_modify(request.user):
            raise Http404
        return super(ArticleEditView, self).dispatch(request, city_name)

    def _display_form(self):
        form = ArticleAddForm(instance=self.article)
        form.patch_rubrics_qs(self.city)

        return render(self.request, 'gorod/forms/article_add.html', {
            'form': form,
            'current_image': self.article.picture,
            'article': self.article
        })


class ArticleDeleteView(View):
    """
        Delete article
    """

    @method_decorator(login_required)
    def dispatch(self, request, city_name, article_id):
        article = get_object_or_404(Article, id=article_id, city__name=city_name)

        if not article.can_user_modify(request.user):
            raise Http404

        try:
            article.delete()
            return HttpResponseRedirect(reverse('gorod:city-main-page', kwargs={'city_name': city_name}))
        except IntegrityError:
            raise Http404


class FeedAPIView(View):
    """
        Get json feed by specifying filters via post parameters
    """
    def dispatch(self, request):
        city_name = request.GET.get('city')
        rubric_name = request.GET.get('rubric')
        filter_name = request.GET.get('filter')
        user_id = request.GET.get('user')
        author_id = request.GET.get('author')

        page = int(request.GET.get('page', 0))
        limit = int(request.GET.get('limit', 15))

        city = get_object_or_404(City, name=city_name)

        filters = {
            'city': city.id,
            'is_published': True,
            'is_checked': True
        }

        if rubric_name:
            rubric = get_object_or_404(ArticleRubric, name=rubric_name, city__name=city_name)
            filters['rubric'] = rubric.id

        if author_id:
            filters['user'] = author_id

        # Applying group filter
        if filter_name:
            if ArticleRubric.is_valid_filter(filter_name):
                articles = Article.objects.get_by_group_filter(filter_name)
        else:
            articles = Article.objects.order_by('-add_date')

        # Apply default filters
        articles = articles.filter(**filters)\
                           .select_related('rubric', 'user', 'donc_data', 'comments')\

        try:
            # TODO: rewrite on queryset input when will be necessary
            json_response = Article.objects.construct_json_feed(articles, page, limit, user_id)
        except FeedError:
            return HttpResponse("{}", mimetype='application/json', status=404)

        return HttpResponse(json_response, mimetype='application/json')
