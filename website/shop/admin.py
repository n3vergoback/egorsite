from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


admin.site.unregister(Group)

@admin.register(Watches)
class Watches_list(admin.ModelAdmin):
    list_display = ('name', 'brand', 'series', 'price', 'sex', 'created_at')
    list_display_links = ('name','brand', 'series')
    search_fields = ('name','brand', 'series')


@admin.register(Phones)
class Phones_list(admin.ModelAdmin):
    list_display = ('brand', 'series', 'price', 'screen_diagonal', 'created_at')
    list_display_links = ('brand', 'series')
    search_fields = ('brand', 'series')


@admin.register(WatchesMechanism)
class WatchesMechanism_list(admin.ModelAdmin):
    list_display = ('mechanism',)
    list_display_links = ('mechanism',)
    search_fields = ('mechanism',)


@admin.register(WatchesCompany)
class WatchesCompany_list(admin.ModelAdmin):
    list_display = ('company',)
    list_display_links = ('company',)
    search_fields = ('company',)
