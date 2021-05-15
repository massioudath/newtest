from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acc_sp30', views.Opendnsv4StatViewSet, basename='acc_sp30')
urlpatterns = [
    url(r'', include(router.urls)),
]
