from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader


from gorod.models import City, CityInfo


# City info/about
def info(request, city_name):
    """ city info view """
    #FIXME
    city = get_object_or_404(City, name=city_name)

    info = get_object_or_404(CityInfo, city__name=city_name)
   
    context = {
        'info': info,
        'city': city 
    }

    return render(request, 'gorod/city_info.html', context)



