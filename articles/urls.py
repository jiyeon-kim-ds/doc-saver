from django.urls    import path, include
from rest_framework import routers

from articles.views import ArticleViewSet

app_name = 'articles'

article_router = routers.SimpleRouter()

article_router.register('', ArticleViewSet, basename='Article')

urlpatterns = [
    path('', include(article_router.urls))
]
