from django.contrib import admin
from django.urls import path,include
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('New/create/',addNews.as_view()),
    path('New/all/',allNew.as_view()),
    path('New/delete/<str:pk>/',DeleteNew.as_view(), name="delete"),
    path('New/update/<str:pk>/',UpdateNew.as_view(), name = "update"),
    path('New/get/<str:pk>',NewGet.as_view(), name = 'newGet'),
    path('api/account/create/', AccountCreateApi.as_view()),
    path('api/user/create/', UserCreateApi.as_view()),
    path('api/supplier/create/', SupplierCreateApi.as_view()),
    path('api/account/update/<str:pk>', AccountUpdateApi.as_view()),
    path('api/user/update/<str:pk>', UserUpdateApi.as_view()),
    path('api/supplier/update/<str:pk>', SupplierUpdateApi.as_view()),
    path('api/account/retrieve/<str:pk>', AccountRetrieveApi.as_view()),
    path('api/user/retrieve/<str:pk>', UserRetrieveApi.as_view()),
    path('api/supplier/retrieve/<str:pk>', SupplierRetrieveApi.as_view()),
    path('api/account/retrieve/auth/', AccountAuthRetrieveApi.as_view())

]

