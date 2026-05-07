from django.urls import path
from .views import *

app_name = 'lectures'

urlpatterns = [
    path('', index, name='index'),
    path('lecture/', lecture_list, name= 'lecture_list'),
    path('professors/', professor_list, name = 'professor_list'),
    path('stu/', student_list, name='student_list')
]