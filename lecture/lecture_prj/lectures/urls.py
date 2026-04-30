from django.urls import path
from .views import *

app_name = 'lectures'

urlpatterns = [
    path('',index, name='index'),
    path('professor-list/', professor, name='professor'),
    path('lecture-list/', lecture, name='lecture'),
    path('student-list/', student, name='student'),
]
