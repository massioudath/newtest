from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acc_sp31', views.RoutingsecStatViewSet, basename='acc_sp31')
urlpatterns = [
    url(r'', include(router.urls)),
]
