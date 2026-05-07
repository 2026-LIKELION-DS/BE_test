from django.urls import path
from .views import professor, lecture, student, index

app_name = 'lectures'

urlpatterns = [
    path('', index, name='index'),
    path('professors/', professor, name='professor'),
    path('lectures/', lecture, name='lecture'),
    path('students/', student, name='student'),
]