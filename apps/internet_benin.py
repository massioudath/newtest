from django.urls import path, include
from django.conf.urls import url


urlpatterns = [

    #route api pour route security au benin
    path('site/', include('apps.check_site.urls')),
    
    #route api pour part de marché des fai au benin
    path('fai/', include('apps.fai_part.urls')),
    
    #route api pour part de marché des operateurs mobile au benin
    path('operateur/', include('apps.operateur_mobile_part.urls')),
    
]
