from django.urls import path
from .views import *

urlpatterns = [
    path('meet/<data_id>', get_meet, name='meet'),
]
