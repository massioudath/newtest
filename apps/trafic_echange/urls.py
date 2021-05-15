from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('echange-point/acc_sp15', views.TraficEchangeViewSet, basename='acc_sp15')


urlpatterns = [
   url(r'', include(router.urls)),
]
