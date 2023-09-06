from django.urls    import path, include
from rest_framework import routers

from tags.views import TagViewSet

app_name = 'tags'

article_router = routers.SimpleRouter()

article_router.register('', TagViewSet, basename='Tag')

urlpatterns = [
    path('', include(article_router.urls))
]
