from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('part_du_marché', views.FaiPartViewSet, basename='fai')


urlpatterns = [
   url(r'', include(router.urls)),
]
