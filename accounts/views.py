from accounts.forms import *
from accounts.service import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from resources.service import *

from .models import *
from .service import *


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user_login = form.cleaned_data['username']
            user_password = form.cleaned_data['password']

            print(user_login, user_password)

            user = authenticate(request, username=user_login, password=user_password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                if User.objects.filter(username=user_login).count() > 0:
                    messages.warning(request, 'Неправильный пароль. Попробуйте еще раз.')
                else:
                    messages.error(request, 'Записи с такими данными не существует. Обратитесь к администратору.')

    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def profile_view(request, profile_id=None):
    if profile_id:
        profile = get_employee(profile_id)
    else:
        profile = get_user_profile(request.user)

    return render(request, 'accounts/profile.html', {'profile': profile})


def division_view(request, division_id):
    division = get_division(division_id)
    employees = get_all_employees().filter(division=division)
    return render(request, 'accounts/division.html', {'division': division, 'employees': employees})


def add_profile(request):
    divisions = get_all_divisions()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['username']:
                if check_username_availability(form.cleaned_data['username']):
                    register_new_user(username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password'],
                                      is_staff=form.cleaned_data['is_staff'],
                                      email=form.cleaned_data['email'],
                                      last_name=form.cleaned_data['last_name'],
                                      first_name=form.cleaned_data['first_name'])
                else:
                    messages.error(request, 'Учетная запись с таким именем пользователя уже существует!')
                    return render(request, 'accounts/profile_editor.html', {'divisions': divisions})

            create_new_employee(last_name=form.cleaned_data['last_name'],
                                first_name=form.cleaned_data['first_name'],
                                middle_name=form.cleaned_data['middle_name'],
                                email=form.cleaned_data['email'],
                                division=form.cleaned_data['division'],
                                username=form.cleaned_data['username'])
            return redirect('profiles')

    return render(request, 'accounts/profile_editor.html', {'divisions': divisions})


def add_division(request):
    if request.method == 'POST':
        form = DivisionForm(request.POST)

        if form.is_valid():
            create_new_division(name=form.cleaned_data['name'], head=form.cleaned_data['head'])
            return redirect('profiles')

    employees = get_all_employees()

    return render(request, 'accounts/division_editor.html', {'employees': employees})


def profiles_view(request):
    employees = get_all_employees()
    divisions = get_all_divisions()

    return render(request, 'accounts/all_profiles.html', {'employees': employees, 'divisions': divisions})
