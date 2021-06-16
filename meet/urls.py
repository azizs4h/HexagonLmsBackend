from django.urls import path
from .views import *

urlpatterns = [
    path('get/<data_id>', get_meet, name='meet'),
    path('add/', add_meet, name='add'),
]
