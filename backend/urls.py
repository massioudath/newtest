"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.conf.urls import url

schema_view = get_swagger_view(title='API Internet Bj')

urlpatterns = [
    path('api/admin/', admin.site.urls),
    
    #route api accounts
    path('api/accounts/', include('apps.accounts.urls')),
    #route api specification accessibilite
    path('api/accessibilite/', include('apps.accessibilite')),
    
    #route api specification abordabilite
    path('api/abordabilite/', include('apps.abordabilite')),
    
    #route api specification disponibilite
    path('api/disponibilite/', include('apps.disponibilite')),
    
    #route api specification marche_internet_benin
    path('api/marche_internet_benin/', include('apps.internet_benin')),
    
    #route api specification security
    path('api/securite/', include('apps.security')),
    
    #Authentification restapi
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    #route token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    
    #route swagger
    url(r'^api/$', schema_view), 
    
]
