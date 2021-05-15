from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    
    #route api ipasn bj
    path('ipasn/', include('apps.ipasnbj.urls')),
    
    #route api domain bj
    path('domain/', include('apps.domainbj.urls')),
    
    #route api penetration bj
    path('penetration/', include('apps.penetrationbj.urls')),
    
    #route api sonde bj
    path('sonde/', include('apps.sondebj.urls')),
    
    
    #route api evolution fai bj
    path('evolution-fai/', include('apps.evolution_fai.urls')),
    
    #route api evolution fixe bj
    path('evolution-fixe/', include('apps.evolution_fixe.urls')),
    
    #route api teledensite  bj
    path('teledensite/', include('apps.teledensitebj.urls')),
 
    #route api trafic echange  bj
    path('trafic/', include('apps.trafic_echange.urls')),
    
    #route api pour openresolver au benin
    path('openresolver/', include('apps.openresolver.urls')),

]
