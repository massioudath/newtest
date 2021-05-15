from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('part_du_marché', views.OperateurMobilePartViewSet, basename='operateur')


urlpatterns = [
   url(r'', include(router.urls)),
]
