from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'lectures'

urlpatterns = [
    path('', index, name='index'),
    path('professor-list', professor_list, name='professor_list'),
    path('lecture-list', lecture_list, name='lecture_list'),
    path('student-list', student_list, name='student_list'),
]