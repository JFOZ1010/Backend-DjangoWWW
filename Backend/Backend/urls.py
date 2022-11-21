"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from AppBack.Api.views import (
                                AccountCreateApi,
                                UserCreateApi, 
                                SupplierCreateApi, 
                                AccountUpdateApi,
                                UserUpdateApi, 
                                SupplierUpdateApi,
                                AccountRetrieveApi,
                                UserRetrieveApi, 
                                SupplierRetrieveApi, 
                                )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/create/', AccountCreateApi.as_view()),
    path('api/user/create/', UserCreateApi.as_view()),
    path('api/supplier/create/', SupplierCreateApi.as_view()),
    path('api/account/update/<int:pk>', AccountUpdateApi.as_view()),
    path('api/user/update/<int:pk>', UserUpdateApi.as_view()),
    path('api/supplier/update/<int:pk>', SupplierUpdateApi.as_view()),
    path('api/account/retrieve/<int:pk>', AccountRetrieveApi.as_view()),
    path('api/user/retrieve/<int:pk>', UserRetrieveApi.as_view()),
    path('api/supplier/retrieve/<int:pk>', SupplierRetrieveApi.as_view()),
]