from django.urls import path
from . import views

urlpatterns = [
    path('emission', views.emission, name='emission'),
    path('programme', views.programme, name='programme'),
    path('prestataire', views.prestataire, name='prestataire'),
]