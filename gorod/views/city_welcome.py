from django.shortcuts import render, get_object_or_404

from django.views.generic import View

from gorod.models import CityWelcome


class CityWelcomeView(View):
    """
        City welcome page
    """
    def dispatch(self, request, city_name):
        info = get_object_or_404(CityWelcome, city__name=city_name)

        context = {
            'welcome': info,
        }

        return render(request, 'gorod/city_welcome.html', context)

