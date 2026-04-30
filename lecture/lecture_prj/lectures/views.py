from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'lectures/index.html')
    
def professor(request):
    professors = Professor.objects.all().order_by('id')
    return render(request, 'lectures/professor_list.html', {'professors': professors})
    
def student(request):
    students = Student.objects.all().order_by('id')
    return render(request,'lectures/student_list.html', {'students': students})

def lecture(request):
    lectures = Lecture.objects.all().order_by('id')
    return render(request,'lectures/lecture_list.html', {'lectures': lectures})


