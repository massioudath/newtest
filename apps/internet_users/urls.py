from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('utilisateurs-internet', views.InternetUsersViewSet, basename='utilisateurs-internet')


urlpatterns = [
   url(r'', include(router.urls)),
]
