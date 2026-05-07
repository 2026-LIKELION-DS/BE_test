from django.contrib import admin
from .models import Professor, Lecture, Student, LectureStudent

admin.site.register(Professor)
admin.site.register(Lecture)    
admin.site.register(Student)
admin.site.register(LectureStudent) 

# Register your models here.
