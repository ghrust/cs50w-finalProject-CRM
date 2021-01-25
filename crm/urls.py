"""URL config for crm app."""

from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet, basename='company')
router.register(r'customers', views.CustomerViewSet, basename='customer')

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('register/',
         views.CreateUserApi.as_view(),
         name=views.CreateUserApi.name),
    path('profile/',
         views.UserDetailAPI.as_view(),
         name=views.UserDetailAPI.name),
]

urlpatterns += router.urls
