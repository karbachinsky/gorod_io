from django.contrib import admin

from gorod.models import City, Article, ArticleRubric, Organization 

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'add_date')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'add_date', 'title', 'city', 'rubric', 'user')


class ArticleRubrucAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'user', 'add_date')



admin.site.register(City, CityAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleRubric, ArticleRubrucAdmin)
admin.site.register(Organization, OrganizationAdmin)


