from django.contrib import admin
from django.urls import path
from AppBack.News.views import addNews,NewGet, allNew, DeleteNew, UpdateNew

from AppBack.Api.accountViews import (
                                AccountCreateApi,
                                AccountUpdateApi,
                                AccountRetrieveApi,
                                AccountAuthRetrieveApi
                                )

from AppBack.Api.userViews import (
                                UserCreateApi, 
                                UserUpdateApi, 
                                UserRetrieveApi, 
                                )

from AppBack.Api.supplierViews import (
                                SupplierCreateApi, 
                                SupplierUpdateApi,
                                SupplierRetrieveApi, 
                                )

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
    path('api/new/create/',addNews.as_view()),
    path('api/new/all/',allNew.as_view()),
    path('api/new/delete/<str:pk>/',DeleteNew.as_view(), name="delete"),
    path('api/new/update/<str:pk>/',UpdateNew.as_view(), name = "update"),
    path('api/new/get/<str:pk>',NewGet.as_view(), name = 'newGet'),
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
    path('api/admin/update_status/<str:pk>', ActivationAdminAPI.as_view()),
    path('api/account/retrieve/auth/', AccountAuthRetrieveApi.as_view()),
]

