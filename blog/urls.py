from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<str:filtre>/<int:id>', views.blog, name="blog"),
    path('search/', views.search, name='search'),
    path('<int:article_id>/single_blog/', views.single_blog, name='single_blog'),
]