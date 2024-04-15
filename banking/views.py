from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from banking.models import *

def index(request):
    return render(request, 'index.html')

def create_account(request):
    if request.method == 'POST':
       
        return HttpResponse('Account created successfully')
    else:
        return render(request, 'create_account.html')

def login(request):
    if request.method == 'POST':
        
        return HttpResponse('Login successful')
    else:
        return render(request, 'login.html')

def dashboard(request):
   
    return render(request, 'dashboard.html')

def withdraw(request):
    if request.method == 'POST':
       
        return HttpResponse('Amount withdrawn successfully')
    else:
        return render(request, 'withdraw.html')

def deposit(request):
    if request.method == 'POST':
       
        return HttpResponse('Amount deposited successfully')
    else:
        return render(request, 'deposit.html')

def change_pin(request):
    if request.method == 'POST':
       
        return HttpResponse('PIN updated successfully')
    else:
        return render(request, 'change_pin.html')
