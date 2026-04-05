from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def welcome(request):
    name = request.GET.get('name')
    year = request.GET.get('year')
    month = request.GET.get('month')
    date = request.GET.get('date')
    age = 2026-int(year)
    
    return render(request, 'welcome.html', {'name': name, 'year' : year, 'month' : month, 'date' : date, 'age' : age})