from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.contrib.auth.models import User
from django.contrib import messages
import datetime

# Create your views here.

def main(request):
    return render(request, "website/main.html")

def app_dsc(request):
    return render(request, "website/app_dsc.html")

def contact(request):
    return render(request, "website/contact.html")

def about(request):
    return render(request, "website/about.html")

def login(request):
    return render(request, "website/login.html")

def register(request):
    return render(request, "website/register.html")

def check_login_data(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login_auth(request, user)
        return redirect('user_page')
    else:
        messages.error(request, "Nie prawidłowe hasło lub nazwa użytkownika", extra_tags="login_status")
        return redirect('login')

def logout(request):
    logout_auth(request)
    return redirect('main')

def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    e_mail = request.POST['e-mail']
    try:
        user = User.objects.create_user(username=username, password=password, email = e_mail)
        user.save()
        messages.success(request, "Pomyślnie założono konto", extra_tags="register_status")
    except:
        messages.error(request, "Taki użytkownik już istnieje", extra_tags="register_status")
    return redirect('register')


def edit_account(request):
    now = datetime.datetime.now()
    days = [i for i in range(1,32)]
    months = ['Styczeń','Luty','Marzec','Kwiecień','Maj','Czerwiec','Lipic','Sierpień','Wrzesień','Październik','Listopad','Grudzień']
    year = [i for i in range(1980, now.year+1)]
    data = {'days': days, 'months': months, 'year': year}
    return render(request, 'website/edit.html', data)


def user_page(request):
    age = [i for i in range(17,100)]
    data = {'age':age}
    return render(request, 'website/after_log.html', data)

def no_log_after(request):
    age = [i for i in range(17,100)]
    data = {'age':age}
    return render(request, "website/no_log_after.html", data)


