from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    
    #route api pour openresolver au benin
    path('openresolver/', include('apps.openresolver.urls')),
    
    #route api pour route security au benin
    path('route-security/', include('apps.route_security.urls')),
    #route api pour route security au benin
    #path('site/', include('apps.test_securiy_site.urls')),
    
    #route api pour route security au benin
    path('site/', include('apps.check_site.urls')),
    
    
    #route api pour cout coupure pendant 24heure
    path('cout/', include('apps.cout_coupure.urls')),

]
