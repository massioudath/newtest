from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acc_sp12', views.TempsInternetViewSet, basename='acc_sp12')


urlpatterns = [
   url(r'', include(router.urls)),
]
