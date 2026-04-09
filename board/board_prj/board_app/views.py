from django.shortcuts import render, redirect
from  .models import *
from  .forms import GuestForm

def board(request): 
    if request.method == 'POST':
        boardform = GuestForm(request.POST)
        if boardform.is_valid():
            boardform.save()
            return redirect('board_app:board')
    else:
        boardform = GuestForm()
    boardlist = Guest.objects.all()
    return render(request, 'board_app/index.html',{'boardform':boardform,'boardlist': boardlist})





