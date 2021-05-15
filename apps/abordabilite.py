from django.urls import path, include
from django.conf.urls import url


urlpatterns = [

    #route api des coût au benin
    path('cout/', include('apps.couts.urls')),

]
