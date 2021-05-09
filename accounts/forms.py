from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=150, required=True)
    password = forms.CharField(label='password', max_length=128, required=True)
