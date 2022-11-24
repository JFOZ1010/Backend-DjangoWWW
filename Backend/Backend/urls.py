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
                                RetreiveAllAccounts,
                                RetreiveAllSuppliers,
                                RetreiveAllUsers,
                                RetreiveAllUserDetailed,
                                RetreiveAllSupsDetailed,
                                ActivationAdminAPI,
                                )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/create/', AccountCreateApi.as_view()),
    path('api/user/create/', UserCreateApi.as_view()),
    path('api/supplier/create/', SupplierCreateApi.as_view()),
    path('api/account/update/<str:pk>', AccountUpdateApi.as_view()),
    path('api/user/update/<str:pk>', UserUpdateApi.as_view()),
    path('api/supplier/update/<str:pk>', SupplierUpdateApi.as_view()),
    path('api/account/retrieve/<str:pk>', AccountRetrieveApi.as_view()),
    path('api/user/retrieve/<str:pk>', UserRetrieveApi.as_view()),
    path('api/supplier/retrieve/<str:pk>', SupplierRetrieveApi.as_view()),
    path('api/account/retreive/all', RetreiveAllAccounts.as_view()),
    path('api/supplier/retreive/all', RetreiveAllSuppliers.as_view()),
    path('api/user/retreive/all', RetreiveAllUsers.as_view()),
    path('api/user/retreive/all/detailed', RetreiveAllUserDetailed.as_view()),
    path('api/supplier/retreive/all/detailed', RetreiveAllSupsDetailed.as_view()),
    path('api/supplier/retreive/all/detailed', RetreiveAllSupsDetailed.as_view()),
    path('api/admin/update_status/<str:pk>', ActivationAdminAPI.as_view()),
]