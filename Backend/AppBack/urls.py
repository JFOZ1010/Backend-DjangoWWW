from django.urls import path
from .views import addNews,NewOverview
  
urlpatterns = [
    path('', NewOverview, name='News'),
    path('create/', addNews, name='addNews'),
]


"""
{   
    "new_title" : "AAAA"
    "new_image" : "SSSSSS"
    "new_description" : "BBBB"
}




"""