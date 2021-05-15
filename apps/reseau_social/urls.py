from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acc_sp12', views.ReseauSocialViewSet, basename='acc_sp12')
router.register('abonnes/acc_sp13', views.NumberUserViewSet, basename='abonnes/acc_sp12')


urlpatterns = [
   url(r'', include(router.urls)),
]
