from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acc_sp10', views.TeledensiteViewSet, basename='acc_sp10')


urlpatterns = [
   url(r'', include(router.urls)),
]
