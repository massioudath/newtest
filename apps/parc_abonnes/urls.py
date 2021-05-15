from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('Fixe/acc_sp5', views.ParcAbonnesFixeViewSet, basename='Fixe/acc_sp5')
router.register('Mobile/acc_sp6', views.ParcAbonnesMobileViewSet, basename='Mobile/acc_sp6')

urlpatterns = [
   url(r'', include(router.urls)),
]
