from django.shortcuts import render,  get_object_or_404, HttpResponsePermanentRedirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.views.generic import View
from django.core.urlresolvers import reverse

from gorod.models import Article

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


class OldUserRedirectView(View):
    """
        Redirect urls like /user/12 -> /city/user/12
    """
    def dispatch(self, request, user_id):
        user = get_object_or_404(get_user_model(), pk=user_id)

        redirect_url = user.get_absolute_url()
        return HttpResponsePermanentRedirect(redirect_url)
