from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acc_sp8', views.RepartitionTechnologieViewSet, basename='acc_sp8')
 
urlpatterns = [
   url(r'', include(router.urls)),
]

