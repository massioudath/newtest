from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('top/acc_sp16', views.TopSiteViewSet, basename='acc_sp16')


urlpatterns = [
   url(r'', include(router.urls)),
]
