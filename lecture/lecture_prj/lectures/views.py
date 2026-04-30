from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'lectures/index.html')

def lecture_list(request):
    lectures = Lecture.objects.all()
    professors = Professor.objects.all()
    return render(request, 'lectures/lecture_list.html', {'lectures':lectures, 'professors':professors})

    

def professor_list(request):
    professors = Professor.objects.all()
    return render(request, 'lectures/professor_list.html', {'professors':professors})

def student_list(request):
    students = Student.objects.all()
    lectures = Lecture.objects.all()
    # 쉼표로 구분해서 한 묶음으로 만듭니다.
    return render(request, 'lectures/student_list.html', {
        'lectures': lectures, 
        'students': students
    })