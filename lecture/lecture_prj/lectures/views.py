from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'lectures/index.html')

def lecture_list(request):
    lectures = Lecture.objects.all()
    return render(request, 'lectures/lecture_list.html', {'lectures':lectures})

def professor_list(request):
    professors = Professor.objects.all()
    return render(request, 'lectures/professor_list.html', {'professors': professors})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'lectures/student_list.html', {'students':students})