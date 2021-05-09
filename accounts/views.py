from accounts.forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


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


def profile_view(request):
    return request
