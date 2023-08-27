from django.urls    import path, include
from rest_framework import routers

from users.views import UserViewSet


app_name = 'users'

user_router = routers.SimpleRouter()

user_router.register('account', UserViewSet)

urlpatterns = [
    path('', include(user_router.urls))
]