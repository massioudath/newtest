from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acc_sp3', views.EvolutionFixeViewSet, basename='acc_sp3')
 
urlpatterns = [
   url(r'', include(router.urls)),
]
