from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from actions.action import Actions
# Register your models here.

class AcceilleAdmin(Actions):
    list_display = ('images_view', 'nom', 'date_add', 'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Gallerie', {'fields': ['nom', 'image', 'description', 'date', 'comentaire', 'vue',]}),
                 ('Standard', {'fields': ['status']})
                 ]


    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))




class FashionAdmin(Actions):
    list_display = ('images_view', 'nom', 'date_add', 'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Gallerie', {'fields': ['nom', 'image', 'description']}),
                 ('Standard', {'fields': ['status']})
                 ]
    


    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class GallerieAdmin(Actions):
    list_display = ('images_view', 'nom', 'date_add', 'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Gallerie', {'fields': ['nom', 'image', 'description']}),
                 ('Standard', {'fields': ['status']})
                 ]


    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class ContactAdmin(Actions):
    list_display =  ('nom','sujet','date_add', 'date_update', 'status',)
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','email','message','sujet',]}),
        ("standare",{'fields':['status',]})
        ]



class NewsLetterAdmin(Actions):
    list_display =  ('date_add', 'date_update','status')
    list_filter =  ('status',)
    date_hierarchy = 'date_add'
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['email',]}),
        ("standare",{'fields':['status',]})
        ]

def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Acceille, AcceilleAdmin)
_register(models.Fashion, FashionAdmin)
_register(models.Gallerie, GallerieAdmin)
_register(models.Contact, ContactAdmin)
_register(models.NewsLetter, NewsLetterAdmin)