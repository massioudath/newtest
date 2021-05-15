from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acc_sp6', views.PenetrationViewSet, basename='acc_sp6')

urlpatterns = [
   url(r'', include(router.urls)),
]
