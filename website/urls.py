from django.urls import path, include
from . import views

from rest_framework import routers
from . import api

router = routers .DefaultRouter()
router.register('acceille',api.AcceilleViewSet)
router.register('fashion',api.FashionViewSet)
router.register('gallerie',api.GallerieViewSet)
router.register('contact',api.ContactViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('news_letter', views.news_letter, name='newsletter'),
    path('api/', include(router.urls)) 
]