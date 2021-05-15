from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acc_sp4', views.IpasnViewSet, basename='acc_sp4')
router.register('asn/acc_sp5', views.IpasnAsnViewSet, basename='acc_sp5')
router.register('ipv4/acc_sp27', views.IpasnIpv4ViewSet, basename='acc_sp27')
router.register('ipv6/acc_sp28', views.IpasnIpv6ViewSet, basename='acc_sp28')
urlpatterns = [
   url(r'', include(router.urls)),
]
