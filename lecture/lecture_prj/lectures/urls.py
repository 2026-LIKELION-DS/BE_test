from django.urls import path
from lectures import views

app_name = 'lectures' 

urlpatterns = [
    path('', views.index, name='index'),
    path('professor-list/', views.professor_list, name="professor-list"),
    path('lectures-list/', views.lectures_list, name="lectures-list"),
    path('student-list/', views.student_list, name="student-list")
]