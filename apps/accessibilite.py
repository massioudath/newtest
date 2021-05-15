from django.urls import path, include
from django.conf.urls import url


urlpatterns = [

    #route api Parc abonnes internet bj
    path('parc-abonnes/', include('apps.parc_abonnes.urls')),
    
    #route api repartition debit bj
    path('repartition-debit/', include('apps.repartition_debit.urls')),
    
    #route api repartition technologie bj
    path('repartition-technologie/', include('apps.repartition_technologie.urls')),
    
    #route api evolution fai bj
    path('evolution-fai/', include('apps.evolution_fai.urls')),
    
    #route api evolution fixe bj
    path('evolution-fixe/', include('apps.evolution_fixe.urls')),
    
    #route api teledensite  bj
    path('teledensite/', include('apps.teledensitebj.urls')),
    
    #route api teledensite  bj
    path('temps-moyens-internet/', include('apps.temps_internet.urls')),
    
    #route api teledensite  bj
    path('reseau-social/', include('apps.reseau_social.urls')),
    
    #route api top site web  bj
    path('site-web/', include('apps.top_site.urls')),
    
    #route api pour  utilisateurs internet
    path('internet/', include('apps.internet_users.urls')),
    
    #route api pour  utilisateurs internet
    path('debit/', include('apps.debit_region.urls')),
    
    #route api pour  utilisateurs internet
    path('user/', include('apps.user_ip.urls')),
    
    
]
