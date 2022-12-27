from django.contrib import admin
from django.urls import path

from AppBack.Api.News.newsViews import (
    addNews,
    NewGet, 
    allNew, 
    DeleteNew, 
    UpdateNew)

from AppBack.Api.Account.accountViews import (
                                AccountCreateApi,
                                AccountUpdateApi,
                                AccountRetrieveApi,
                                AccountAuthRetrieveApi,
                                RetreiveAllAccounts,
                                RetreiveAllUserDetailed,
                                RetreiveAllSupsDetailed,
                                ActivationAdminAPI
                                )

from AppBack.Api.Users.userViews import (
                                UserCreateApi, 
                                UserUpdateApi, 
                                UserRetrieveApi,
                                RetreiveAllUsers,
                                )

from AppBack.Api.Supplier.supplierViews import (
                                SupplierCreateApi, 
                                SupplierUpdateApi,
                                SupplierRetrieveApi, 
                                RetreiveAllSuppliers,
                                )

from AppBack.Api.Item.itemViews import (
                                ItemCreateApi,
                                ItemCreateApi2,
                                AllItems,
                                )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/new/create',addNews.as_view()),
    path('api/new/all',allNew.as_view()),
    path('api/new/delete/<str:pk>',DeleteNew.as_view(), name="delete"),
    path('api/new/update/<str:pk>',UpdateNew.as_view(), name = "update"),
    path('api/new/get/<str:pk>',NewGet.as_view(), name = 'newGet'),
    path('api/account/create', AccountCreateApi.as_view()),
    path('api/user/create', UserCreateApi.as_view()),
    path('api/supplier/create', SupplierCreateApi.as_view()),
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
    path('api/auth/retrieve', AccountAuthRetrieveApi.as_view()),
    path('api/item/create', ItemCreateApi.as_view()),
    path('api/item/create2', ItemCreateApi2.as_view()),
<<<<<<< HEAD
    path('api/item/all', AllItems.as_view()),
=======
    path('api/item/allItems', AllItems.as_view()),
>>>>>>> 96dbe72ba95c41c17f0d626324c4a704ed83b2af
]

