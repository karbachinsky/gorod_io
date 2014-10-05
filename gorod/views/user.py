# -*- coding: utf-8 -*-

from django.shortcuts import render,  get_object_or_404, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.views.generic import View, TemplateView
from django.core.urlresolvers import reverse
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate, login, logout

from gorod.models import Article
from gorod.utils.views.mixins import JSONResponseMixin

USER_LAST_FEEDS_CNT = 10


class ProfileView(View):
    """
       User profile .age/
    """
    def dispatch(self, request, city_name, user_id):
        user = get_object_or_404(get_user_model().objects.select_related(), id=user_id)

        if user.city.name != city_name:
            return HttpResponsePermanentRedirect(user.get_absolute_url())

        user_last_feeds = Article.objects.filter(user__id=user_id)\
                                         .filter(is_published=True)\
                                         .order_by('-add_date')\
                                         .select_related()\
                                         .all()[:USER_LAST_FEEDS_CNT]

        context = {
            'user_info': user,
            'user_last_feeds': user_last_feeds
        }

        return render(request, 'gorod/user/profile.html', context)


class LogoutView(View):
    """
        Logout action.
    """
    def dispatch(self, request):
        try:
            city = request.user.city
            logout(request)
            return HttpResponseRedirect(
                reverse('gorod:city-main-page', kwargs=dict(city_name=city.name))
            )
        except AttributeError:
            # Case when someone tries to logout if he is not authed
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class LoginView(JSONResponseMixin, TemplateView):
    def _post(self, request):
        """
            Process post from login form
        """
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return self.json_success_context()
            else:
                return self.json_form_error_context(_('Ваш аккаунт заблокирован!'))

        return self.json_form_error_context(_('Неверный логин и пароль!'))

    def _get(self, request):
        return self.json_form_error_context(_('Неверный логин и пароль!'))


class OldUserRedirectView(View):
    """
        Redirect urls like /user/12 -> /city/user/12
    """
    def dispatch(self, request, user_id):
        user = get_object_or_404(get_user_model(), pk=user_id)

        redirect_url = user.get_absolute_url()
        return HttpResponsePermanentRedirect(redirect_url)
