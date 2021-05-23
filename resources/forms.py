from accounts.models import *
from django import forms
from resources.models import *


class ResourceForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, required=True)

    admin = forms.CharField(label='admin', max_length=50, required=False)
    owner = forms.CharField(label='owner', max_length=50, required=True)

    facility = forms.CharField(label='facility', max_length=50, required=False)

    description = forms.CharField(label='description', max_length=500, required=False)
    dns_address = forms.CharField(label='dns_address', max_length=100, required=False)

    def clean(self):
        cleaned_data = super().clean()

        if len(cleaned_data['description']) == 0:
            cleaned_data['description'] = None

        if len(cleaned_data['dns_address']) == 0:
            print('ona')
            cleaned_data['dns_address'] = None

        if cleaned_data['admin']:
            cleaned_data['admin'] = Employee.objects.get(id=cleaned_data['admin'])
        else:
            cleaned_data['admin'] = None

        if cleaned_data['facility']:
            cleaned_data['facility'] = Facility.objects.get(id=cleaned_data['facility'])
        else:
            cleaned_data['facility'] = None


class FacilityForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, required=True)

    admin = forms.CharField(label='admin', max_length=50, required=False)
    owner = forms.CharField(label='owner', max_length=50, required=True)
    location = forms.CharField(label='location', max_length=100, required=True)

    description = forms.CharField(label='description', max_length=500, required=False)
    dns_address = forms.CharField(label='dns_address', max_length=100, required=False)

    def clean(self):
        cleaned_data = super().clean()

        if len(cleaned_data['description']) == 0:
            cleaned_data['description'] = None

        if len(cleaned_data['dns_address']) == 0:
            cleaned_data['dns_address'] = None

        if cleaned_data['admin']:
            cleaned_data['admin'] = Employee.objects.get(id=cleaned_data['admin'])
        else:
            cleaned_data['admin'] = None
