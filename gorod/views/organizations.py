from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from gorod.models import City, Organization


class OrganizationsView(View):
    """
        City organizations list page.
    """
    def dispatch(self, request, city_name):
        organizations = Organization.objects.filter(city__name=city_name)\
                                            .order_by('name')\
                                            .select_related()

        context = {
            'organizations': organizations,
        }

        return render(request, 'gorod/organizations.html', context)


class OrganizationView(View):
    """
        Certain organization page.
    """
    def dispatch(self, request, city_name, organization_id):
        organization = get_object_or_404(Organization, pk=organization_id, city__name=city_name)

        context = {
            'organization': organization,
        }

        return render(request, 'gorod/organization.html', context)

