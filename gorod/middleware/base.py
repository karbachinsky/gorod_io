from django.core.urlresolvers import resolve, Resolver404
from django.http import HttpResponsePermanentRedirect, Http404
from gorod.models import City

class UserCityMiddleware(object):
    """ 
        Set user city if he is authorized 
        ans city is not set yet
    """
    def __init__(self):
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.user.is_authenticated() or request.user.city:
            return None

        city = None
        current_url_params = request.resolver_match.kwargs

        if current_url_params.get('city_name'):
            city = City.objects.get(name=current_url_params.get('city_name'));

        if not city:
            return None

        try:
            request.user.city = city
            request.user.save()
        # FIXME
        except Exception as e:
            raise e

        return None


class RedirectOldCityUrlsMiddleware(object):
    """
        Redirect old urls with /town/$city/*  to /$city/*
    """
    def process_request(self, request):
        if request.path in ('/towns/', '/archive/'):
            return HttpResponsePermanentRedirect('/')

        if not request.path.startswith('/town'):
            return None

        redirect_url = request.path.replace('/town', '', 1)

        try:
            resolve(redirect_url)
            return HttpResponsePermanentRedirect(redirect_url)
        except Resolver404:
            raise Http404('Bad url')