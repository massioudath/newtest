from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('internet-fixe/acc_sp7', views.RepartitionInternetFixeDebitViewSet, basename='acc_sp7')
 
urlpatterns = [
   url(r'', include(router.urls)),
]
