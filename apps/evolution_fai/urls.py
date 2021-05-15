from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acc_sp2', views.EvolutionFaiViewSet, basename='acc_sp2')

urlpatterns = [
   url(r'', include(router.urls)),
]
