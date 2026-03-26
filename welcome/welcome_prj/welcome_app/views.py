from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def welcome(request):
    name=request.GET.get('name')
    birthyear=request.GET.get('birthyear')
    birthmonth=request.GET.get('birthmonth')
    birthday=request.GET.get('birthday')

    age=2025-int(birthyear)
    
    return render(request, "welcome.html",{"nametext":name,"yeartext":birthyear,"monthtext":birthmonth,"daytext":birthday,"agetext":age})



