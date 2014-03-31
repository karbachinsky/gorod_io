from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader


from gorod.models import City, Organization


# City organizations 
def organizations(request, city):
    city = get_object_or_404(City, name=city)
   
    organizations = Organization.objects.filter(city=city.id).order_by('name').all 

    context = {
        'organizations': organizations,
        'city': city 
    }

    return render(request, 'gorod/organizations.html', context)



# One organization view
def organization(request, organization_id): 
    organization = get_object_or_404(Organization, pk=organization_id)

    city = get_object_or_404(City, id=organization.city.id)

    context = {
        'organization': organization,
        'city': city
    }

    return render(request, 'gorod/organization.html', context)

