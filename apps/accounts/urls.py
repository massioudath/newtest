from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

router = DefaultRouter()
router.register('users', views.UserViewSet, basename='user-list')

urlpatterns = [
    path('', include(router.urls)),
    #path('account/logout/', views.LogoutView.as_view(), name='logout'),
]
