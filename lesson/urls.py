from django.urls import path
from .views import *

urlpatterns = [
    path('', LessonsView.as_view(), name='lesson'),
    path('info/', LessonsInfoView.as_view(), name='lessoninfo'),
    path('notes/', LessonNotesView.as_view(), name='notes'),

]
