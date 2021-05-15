from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('Cout-Fibre-Optique/acc_sp17', views.CoutFibreOptiqueViewSet, basename='acc_sp17')
router.register('Cout-Adsl/acc_sp18', views.CoutAdslViewSet, basename='acc_sp18')
router.register('Cout-Go-Internet-Mobile/acc_sp19', views.CoutGoInternetMobileViewSet, basename='acc_sp19')
router.register('Licence-Fai/acc_sp20', views.LicenceFaiViewSet, basename='acc_sp20')
router.register('Licence-Gsm/acc_sp21', views.LicenceGsmViewSet, basename='acc_sp21')


urlpatterns = [
   url(r'', include(router.urls)),
   url(r'Cout-Go-Internet-Mobile/max/acc_sp22', views.CoutGoInternetMobileView.as_view()),
]
