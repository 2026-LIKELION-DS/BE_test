from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')    

def welcome(request):
    user_name = request.GET['name_input']
    user_year = request.GET['year_input']
    user_month = request.GET['month_input']
    user_day = request.GET['day_input']
    user_age = 2025-int(user_year)
    
    return render(request, 'welcome.html', 
    {'name': user_name, 
    'year':user_year, 
    'month':user_month,
    'day':user_day, 
    'age':user_age})


