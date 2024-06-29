from django.urls import path
from . import views
urlpatterns = [
    path('paint', views.paint, name='paint'),
    #path('files', views.files, name='files'),
   # path('search', views.search, name='search'),
]