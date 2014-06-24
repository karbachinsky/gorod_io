from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from mptt.admin import MPTTModelAdmin

from gorod.models import User
from gorod.models import City
from gorod.models import Article
from gorod.models import ArticleRubric

from gorod.models import Organization
from gorod.models import OrganizationCategory
from gorod.models import OrganizationAddress
from gorod.models import OrganizationPhone
from gorod.models import OrganizationSchedule

from gorod.models import CityInfo


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


class GorodUserCreationForm(UserCreationForm):
    pass


class GorodUserChangeForm(UserChangeForm):
    pass


class GorodUserAdmin(UserAdmin):
    form = GorodUserChangeForm
    add_form = GorodUserCreationForm

    # Redefining fields adding profile fields like city
    # May we should just append these fields to default?
    fieldsets = (
        (None, {'fields': ('username', 'password', 'city')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'avatar')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'city')}
        ),
    )


class CityAdmin(GorodAdminBase):
    list_display = ('id', 'name', 'title', 'add_date')


class CityInfoAdmin(GorodAdminBase):
    list_display = ('id', 'city')


class ArticleAdmin(GorodAdminBase):
    list_display = ('id', 'add_date', 'title', 'city', 'rubric', 'user', 'is_checked')


class ArticleRubrucAdmin(GorodAdminBase):
    list_display = ('id', 'name')


class OrganizationAddressInline(admin.StackedInline):
    model = OrganizationAddress
    extra = 1

class OrganizationPhoneInline(admin.StackedInline):
    model = OrganizationPhone
    extra = 1

class OrganizationScheduleInline(admin.StackedInline):
    model = OrganizationSchedule
    extra = 2

class OrganizationAdmin(GorodAdminBase):
    list_display = ('id', 'name', 'city', 'user', 'add_date')
    inlines = [OrganizationAddressInline, OrganizationPhoneInline, OrganizationScheduleInline]
    mptt_indent_field = "category"


class OrganizationCategoryAdmin(MPTTModelAdmin):
    list_display = ('id', 'name', 'title')
    mptt_level_indent = 20


class OrganizationScheduleAdmin(GorodAdminBase):
    list_display = ('id', 'time_from')

admin.site.register(OrganizationSchedule, OrganizationScheduleAdmin)


admin.site.register(User, GorodUserAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(CityInfo, CityInfoAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleRubric, ArticleRubrucAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationCategory, OrganizationCategoryAdmin)

