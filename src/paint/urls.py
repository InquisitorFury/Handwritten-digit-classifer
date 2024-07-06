from django.urls import path
from .views import PaintView

urlpatterns = [
    path('', PaintView.as_view(), name='paint'),
   
]
