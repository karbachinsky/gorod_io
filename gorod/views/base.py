from django.shortcuts import render
from django.views.generic import View

from gorod.models import City


class JsonMixin(object):
    """
        Mixin to be used in view that provide json api with ?jsonapi parameter in url
    """
    def dispatch(self, request, *args, **kwargs):
        if self.request.GET['jsonapi']:
            pass


class IndexView(View):
    """
        Gorod main page
    """
    def dispatch(self, request, *args, **kwargs):
        cities = City.objects.order_by('title').all

        context = {
            'cities': cities
        }

        return render(request, 'gorod/index.html', context)


def handler404(request):
    return render(request, '404.html')


def handler500(request):
    return render(request, '500.html')


