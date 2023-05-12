from django.shortcuts import render, redirect
from .models import Expense
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('expense_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required(login_url='/login/')
def add_expense(request):
    if request.method == 'POST':
        title = request.POST['title']
        amount = request.POST['amount']
        category = request.POST['category']
        Expense.objects.create(user=request.user, title=title, amount=amount, category=category)
        return redirect('expense_list')
    return render(request, 'add_expense.html')

@login_required(login_url='/login/')
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expense_list.html', {'expenses': expenses})

@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect('login')
