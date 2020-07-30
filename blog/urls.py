from django.urls import path, include
from . import views

from rest_framework import routers
from . import api

router = routers .DefaultRouter()
router.register('categories',api.CategorieArticleViewSet)
router.register('tags',api.TagViewSet)
router.register('articles',api.ArticleViewSet)
router.register('commentaires',api.CommentaireViewSet)



urlpatterns = [
    path('', views.blog, name='blog'),
    path('<str:filtre>/<int:id>', views.blog, name="blog"),
    path('search/', views.search, name='search'),
    path('<int:article_id>/single_blog/', views.single_blog, name='single_blog'),
    path('api/', include(router.urls))
]