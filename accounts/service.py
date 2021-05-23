from .models import *


def get_all_employees():
    items = Employee.objects.filter().order_by('last_name')
    return items


def get_employee(employee_id):
    item = Employee.objects.get(id=employee_id)
    return item


def get_user_profile(user):
    item = Employee.objects.get(account_id=user.id)
    return item
