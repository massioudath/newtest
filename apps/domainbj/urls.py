from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acc_sp1', views.DomainViewSet, basename='acc_sp1')

urlpatterns = [
   url(r'', include(router.urls)),
]
