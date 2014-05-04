from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from gorod.models import City, Article, ArticleRubric, Organization, OrganizationCategory, CityInfo


class GorodAdminBase(admin.ModelAdmin):

    def response_add(self, request, obj):
        """ Redirect to object's page after add if exists param source  = main """
        return self._response_add_and_change(request, obj)

    def response_change(self, request, obj):
        """ Redirect to object's page after save change if exists param source = main """
        return self._response_add_and_change(request, obj)

    def _response_add_and_change(self, request, obj):
        """ if user clicked "edit this page" or 'add page ' return to obj's page  after save """
        response = super(GorodAdminBase, self).response_change(request, obj)

        if (isinstance(response, HttpResponseRedirect) and
            request.GET.get('source') == 'main'):
                response['location'] = reverse(
                    'gorod:' + self._url_name_by_object(obj), 
                    args=[obj.city.name, obj.id]
                    #kwargs={'article_id': obj.id, 'city_name': obj.city.name}
                )

        return response

    def _url_name_by_object(self, obj):
        """ get url name for object by it's class name"""
        return obj.__class__.__name__.lower()


class CityAdmin(GorodAdminBase):
    list_display = ('id', 'name', 'title', 'add_date')


class CityInfoAdmin(GorodAdminBase):
    list_display = ('id', 'city')


class ArticleAdmin(GorodAdminBase):
    list_display = ('id', 'add_date', 'title', 'city', 'rubric', 'user')


class ArticleRubrucAdmin(GorodAdminBase):
    list_display = ('id', 'name')


class OrganizationAdmin(GorodAdminBase):
    list_display = ('id', 'name', 'city', 'user', 'add_date')

class OrganizationCategoryAdmin(GorodAdminBase):
    list_display = ('id', 'name', 'title')



admin.site.register(City, CityAdmin)
admin.site.register(CityInfo, CityInfoAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleRubric, ArticleRubrucAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationCategory, OrganizationCategoryAdmin)

