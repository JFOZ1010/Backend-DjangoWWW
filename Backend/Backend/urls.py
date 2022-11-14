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
                                AccountUserCreateApi, 
                                AccountSupplierCreateApi, 
                                AccountUserUpdateApi, 
                                AccountUserRetreiveApi,
                                AccountSupplierUpdateApi,
                                AccountSupplierRetreiveApi
                                )
#Kevin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account_users/create/', AccountUserCreateApi.as_view()),
    path('api/account_users/update/<int:pk>', AccountUserUpdateApi.as_view()),
    path('api/account_users/retrieve/<int:pk>', AccountUserRetreiveApi.as_view()),
    path('api/account_suppliers/create/', AccountSupplierCreateApi.as_view()),
    path('api/account_suppliers/update/<int:pk>', AccountSupplierUpdateApi.as_view()),
    path('api/account_suppliers/retrieve/<int:pk>', AccountSupplierRetreiveApi.as_view()),
    
]