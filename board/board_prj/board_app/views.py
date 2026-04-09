from django.shortcuts import render, redirect
from .forms import *
from .models import Guest
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_app:index')
    else:
        form = GuestForm()
    guest = Guest.objects.all()    
    return render(request,'board_app/index.html',{'form':form, 'guest':guest})