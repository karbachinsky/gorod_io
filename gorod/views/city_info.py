from django.shortcuts import render, get_object_or_404

from django.views.generic import View

from gorod.models import City, CityInfo


class CityInfoView(View):
    """
        City info/about.
    """
    def dispatch(self, request, city_name):
        info = get_object_or_404(CityInfo, city__name=city_name)

        context = {
            'info': info,
        }

        return render(request, 'gorod/city_info.html', context)

