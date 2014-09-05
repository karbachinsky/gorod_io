from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django_mptt_admin.admin import DjangoMpttAdmin
#from mptt.admin import MPTTModelAdmin

from gorod.models import *


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
                try:  
                    response['location'] = obj.get_absolute_url()
                # FIXME
                except Exception:
                    pass

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

    list_display = ('id', 'is_staff', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'city')

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
            'fields': ('username', 'password1', 'password2', 'city')
        }),
    )
    ordering = ['-date_joined']

class CityAdmin(GorodAdminBase):
    list_display = ('id', 'name', 'title', 'add_date')


## CITYINFO


#class CityInfoQuestionInline(admin.StackedInline):
#    model = CityInfoQuestion
#    extra = 2


#class CityInfoAdmin(GorodAdminBase):
#    list_display = ('id', 'city')
#    inlines = [CityInfoQuestionInline]


## HUB

class HubAnswerInline(admin.StackedInline):
    model = HubAnswer
    extra = 2


class HubQuestionAdmin(GorodAdminBase):
    list_display = ('id', 'city', 'question')
    inlines = [HubAnswerInline]


class CityWelcomeAdmin(GorodAdminBase):
    list_display = ('id', 'city')


## ARTICLES
class ArticleAdmin(GorodAdminBase):
    def view_link(self, obj):
        obj_url = obj.url
        return u"<a href='%s' target='blank'>%s</a>" % (obj_url, obj_url)

    view_link.allow_tags = True
    readonly_fields = ('short_text',)
    list_display = ('id', 'add_date', 'title', 'city', 'rubric', 'user', 'view_link', 'is_checked')
    save_on_top = True
    view_on_site = True


class ArticleRubrucAdmin(GorodAdminBase):
    list_display = ('id', 'name')


## ORGANIZATIONS

class OrganizationAddressInline(admin.StackedInline):
    model = OrganizationAddress
    extra = 1
    max_num = 1


class OrganizationPhoneInline(admin.StackedInline):
    model = OrganizationPhone
    extra = 1
    max_num = 1


class OrganizationScheduleInline(admin.StackedInline):
    model = OrganizationSchedule
    extra = 2


class OrganizationAdmin(GorodAdminBase):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = OrganizationCategory.objects.get_first_level_categories()
        return super(OrganizationAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def view_link(self, obj):
        obj_url = obj.get_absolute_url()
        return u"<a href='%s' target='blank'>%s</a>" % (obj_url, obj_url)

    view_link.allow_tags = True
    list_display = ('id', 'name', 'city', 'user', 'view_link', 'add_date')
    #inlines = [OrganizationAddressInline, OrganizationPhoneInline, OrganizationScheduleInline]
    inlines = [OrganizationAddressInline, OrganizationPhoneInline]
    mptt_indent_field = "category"
    save_on_top = True
    view_on_site = True


class OrganizationCategoryAdmin(DjangoMpttAdmin):
    list_display = ('id', 'name', 'title')
    mptt_level_indent = 20


class OrganizationScheduleAdmin(GorodAdminBase):
    list_display = ('id', 'time_from')


class ComplaintAdmin(GorodAdminBase):
    list_display = ('id', 'city', 'email', 'add_date')
    readonly_fields = ('comment', 'city', 'add_date', 'url', 'type', 'email')


# Change list display for social auths.
from social.apps.django_app.default.admin import UserSocialAuthOption


def social_user_city(self, obj):
    return obj.user.city


def social_user_email(self, obj):
    return obj.user.email


def social_user_date_joined(self, obj):
    return obj.user.date_joined

setattr(UserSocialAuthOption, 'city', social_user_city)
setattr(UserSocialAuthOption, 'email', social_user_email)
setattr(UserSocialAuthOption, 'date_joined', social_user_date_joined)
UserSocialAuthOption.list_display = ('id', 'user', 'email', 'provider', 'city', 'date_joined')
UserSocialAuthOption.list_select_related = ('user',)



admin.site.register(OrganizationSchedule, OrganizationScheduleAdmin)
admin.site.register(User, GorodUserAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(HubQuestion, HubQuestionAdmin)
#admin.site.register(CityInfo, CityInfoAdmin)
admin.site.register(CityWelcome, CityWelcomeAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleRubric, ArticleRubrucAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationCategory, OrganizationCategoryAdmin)
admin.site.register(Complaint, ComplaintAdmin)

## Ckeditor to flatpages

from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

# Note: we are renaming the original Admin and Form as we import them!
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

from django import forms
from ckeditor.widgets import CKEditorWidget


class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FlatPage # this is not automatically inherited from FlatpageFormOld


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm


# We have to unregister the normal admin, and then reregister ours
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
