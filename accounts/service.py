from django.contrib.auth.models import Group, User

from .models import *


def get_all_employees():
    items = Employee.objects.filter().order_by('division', 'last_name')
    return items


def get_all_divisions():
    items = Division.objects.filter()
    return items


def get_division(division_id):
    item = Division.objects.get(id=division_id)
    return item


def create_new_employee(last_name, first_name, email, username=None, middle_name=None, division=None):
    user = Employee.objects.create(last_name=last_name,
                                   first_name=first_name,
                                   middle_name=middle_name,
                                   email=email,
                                   division=division)

    if username:
        user.account = User.objects.get(username=username)

    user.save()


def create_new_division(name, head):
    division = Division.objects.create(name=name,
                                       head=head)
    head.division = division
    head.save()
    division.save()


def get_employee(employee_id):
    item = Employee.objects.get(id=employee_id)
    return item


def get_user_profile(user):
    item = Employee.objects.get(account_id=user.id)
    return item


def check_username_availability(username):
    if User.objects.filter(username=username).exists():
        return False
    else:
        return True


def register_new_user(username, password, is_staff, email, last_name, first_name, is_superuser=None):
    user = User.objects.create_user(username=username, email=email, is_staff=is_staff, last_name=last_name,
                                    first_name=first_name, password=password)
    if is_superuser:
        group = Group.objects.get(name='Администратор')
    elif is_staff:
        group = Group.objects.get(name='Оператор')
    else:
        group = Group.objects.get(name='Пользователь')
    group.user_set.add(user)

    user.save()
