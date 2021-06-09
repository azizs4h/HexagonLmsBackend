from django.urls import path
from .views import *

urlpatterns = [
    path('u/<user_id>', get_lessons, name='lesson'),
    path('info/<data_id>', lesson_info, name='lessoninfo'),
    path('notes/<data_id>', lesson_notes, name='notes'),
    path('notes/delete/<data_id>', lesson_notes, name='notes'),
    path('notes/add/', add_lesson_notes, name='notes'),
]
