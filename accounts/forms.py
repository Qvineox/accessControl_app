from django import forms
from django.contrib import messages

from .models import Division, Employee


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=150, required=True)
    password = forms.CharField(label='password', max_length=128, required=True)


class DivisionForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, required=True)
    head = forms.CharField(label='head', required=True)

    def clean(self):
        cleaned_data = super().clean()

        cleaned_data['head'] = Employee.objects.get(id=cleaned_data['head'])


class EmployeeForm(forms.Form):
    last_name = forms.CharField(label='last_name', max_length=50, required=True)
    first_name = forms.CharField(label='first_name', max_length=50, required=True)
    middle_name = forms.CharField(label='middle_name', max_length=50, required=False)

    email = forms.CharField(label='email', max_length=100, required=True)

    division = forms.CharField(label='division', required=False)

    username = forms.CharField(label='username', max_length=150, required=False)
    status = forms.CharField(label='status', required=False)
    password = forms.CharField(label='password', max_length=20, required=False)
    password_repeat = forms.CharField(label='password_repeat', max_length=20, required=False)

    def clean(self):
        cleaned_data = super().clean()

        if len(cleaned_data['division']) == 0:
            cleaned_data['division'] = None
        else:
            cleaned_data['division'] = Division.objects.get(id=cleaned_data['division'])

        if len(cleaned_data['middle_name']) == 0:
            cleaned_data['middle_name'] = None

        if cleaned_data['username']:
            if cleaned_data['status'] == 'operator':
                cleaned_data['is_staff'] = True
            else:
                cleaned_data['is_staff'] = False
        else:
            cleaned_data['username'] = None
