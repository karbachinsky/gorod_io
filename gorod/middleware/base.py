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
            city = City.objects.get(name=current_url_params.get('city_name'))

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
        if any(map(lambda x: x in request.path, ('/admin', '/media'))):
            return

        redirects = ('_redirect_towns', '_redirect_pk', '_redirect_hub')

        for func in redirects:
            redirect = getattr(self, func)(request)
            if redirect:
                return redirect

        return None

    def _redirect_pk(self, request):
        """
            PK -> pk
        """
        if not '/PK' in request.path:
            return None

        redirect_url = request.path.replace('/PK', '/pk', 1)

        return self._resolve_redirect_url(redirect_url)

    def _redirect_hub(self, request):
        """
            hub -> question
        """
        if not '/hub' in request.path:
            return None

        redirect_url = request.path.replace('/hub', '/question', 1)

        return self._resolve_redirect_url(redirect_url)


    def _redirect_towns(self, request):
        """
            Redirect /towns/ /archive /town/*
        """
        if request.path in ('/towns/', '/archive/'):
            return HttpResponsePermanentRedirect('/')

        if not request.path.startswith('/town'):
            return None

        redirect_url = request.path.replace('/town', '', 1)

        return self._resolve_redirect_url(redirect_url)

    @staticmethod
    def _resolve_redirect_url(url):
        try:
            resolve(url)
            return HttpResponsePermanentRedirect(url)
        except Resolver404:
            raise Http404('Bad url!')