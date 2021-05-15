from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acc_sp9', views.SondeViewSet, basename='acc_sp9')
 
urlpatterns = [
   url(r'', include(router.urls)),
]
