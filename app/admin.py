from cgitb import html
from os import name
from django.contrib import admin
from .models import Blog, Category,Product, Portfolio, Hizmetler, Kurumsal, TagDict
from django.utils.safestring import mark_safe

class BlogAdmin(admin.ModelAdmin):
    list_display= ("title","is_active","is_home","slug","selected_categories",)
    list_editable= ("is_active","is_home",)
    search_fields= ("title","description")
    readonly_fields= ("slug",)
    list_filter= ("is_active","is_home","categories",)

    def selected_categories(self, obj):
        html= "<ul>"
        for category in obj.categories.all():
            html+= "<li>" + category.name + "</li>"

        html+= "</ul>"
        return mark_safe(html)


class ProductAdmin(admin.ModelAdmin):
    list_display= ("title","is_active","is_home","slug",)
    list_editable= ("is_active","is_home",)
    search_fields= ("title","description")
    readonly_fields= ("slug",)
    list_filter= ("is_active","is_home",)

class PortfolioAdmin(admin.ModelAdmin):
    list_display= ("name","is_active","is_home","slug",)
    list_editable= ("is_active","is_home",)
    search_fields= ("name","description",)
    readonly_fields= ("slug",)
    list_filter= ("is_active","is_home",)


class HizmetlerAdmin(admin.ModelAdmin):
    list_display= ("name","is_active","is_home","slug",)
    list_editable= ("is_active","is_home",)
    search_fields= ("name","description",)
    readonly_fields= ("slug",)
    list_filter= ("is_active","is_home",)

class KurumsalAdmin(admin.ModelAdmin):
    list_display= ("name","id")

admin.site.register(Kurumsal, KurumsalAdmin)
admin.site.register(Hizmetler, HizmetlerAdmin)
admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
admin.site.register(TagDict)
admin.site.register(Product,ProductAdmin)

