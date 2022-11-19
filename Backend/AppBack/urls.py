from django.urls import path
from .views import addNews,NewOverview, allNews, updateNew, deleteNew
  
urlpatterns = [
    path('', NewOverview, name='News'),
    path('create/', addNews, name='addNews'),
    path('all/', allNews, name='allNews'),
    path('update/<str:pk>/', updateNew, name='updateNew'),
    path('delete/<str:pk>/', deleteNew, name='deleteNew'),
]


"""
{   
    "new_title" : "AAAA"
    "new_image" : "SSSSSS"
    "new_description" : "BBBB"
}




"""