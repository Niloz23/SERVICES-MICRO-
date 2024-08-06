"""
URL configuration for project(ads) project(ads).

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from adservice.views import *

router = DefaultRouter()
router.register(r'ads', AdViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/', UserListView.as_view(), name='user-list'),
    path('ad', Ad_list, name='ad_list'),
    path('ad/new/', Ad_create, name='ad_create'),
    path('ad/edit/<int:pk>/', Ad_edit, name='ad_edit'),
    path('ad/delete/<int:pk>/', Ad_delete, name='ad_delete'),
]