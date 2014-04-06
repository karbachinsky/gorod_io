from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader


from gorod.models import City, Organization


# City organizations 
def organizations(request, city_name):
    city = get_object_or_404(City, name=city_name)
   
    organizations = Organization.objects.filter(city=city.id).order_by('name').all 

    context = {
        'organizations': organizations,
        'city': city 
    }

    return render(request, 'gorod/organizations.html', context)



# One organization view
def organization(request, city_name, organization_id): 
    city = get_object_or_404(City, name=city_name)
    organization = get_object_or_404(Organization, pk=organization_id, city=city.id)

    context = {
        'organization': organization,
        'city': city
    }

    return render(request, 'gorod/organization.html', context)

