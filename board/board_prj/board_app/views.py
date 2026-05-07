from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board:index')
    else:
        form = GuestForm()
    
    guests= Guest.objects.all()
    return render(request, 'board_app/index.html', {'form': form , 'guests': guests})
