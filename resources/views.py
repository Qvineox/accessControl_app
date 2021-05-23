from django.shortcuts import render, redirect
from home.models import *
from home.service import *

from .forms import *
from .service import *


def resources_view(request):
    resources = get_all_resources()
    return render(request, 'resources/resources_dashboard.html', {'resources': resources})


def add_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)

        if form.is_valid():
            new_resource = Resource.objects.create(name=form.cleaned_data['name'],
                                                   owner=Employee.objects.get(id=form.cleaned_data['owner']),
                                                   admin=form.cleaned_data['admin'],
                                                   facility=form.cleaned_data['facility'],
                                                   description=form.cleaned_data['description'],
                                                   DNS_address=form.cleaned_data['dns_address'])
            new_resource.save()
            return redirect('resources')

    employees = get_all_employees()
    facilities = get_all_facilities()

    return render(request, 'resources/resource_editor.html', {'employees': employees, 'facilities': facilities})


def add_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)

        if form.is_valid():
            new_facility = Facility.objects.create(name=form.cleaned_data['name'],
                                                   owner=Employee.objects.get(id=form.cleaned_data['owner']),
                                                   admin=form.cleaned_data['admin'],
                                                   location=form.cleaned_data['location'],
                                                   description=form.cleaned_data['description'],
                                                   DNS_address=form.cleaned_data['dns_address'])
            new_facility.save()
            return redirect('resources')

    employees = get_all_employees()

    return render(request, 'resources/facility_editor.html', {'employees': employees})


def resource_view(request, resource_id):
    resource = ger_resource(resource_id)
    return render(request, 'resources/resource_page.html', {'resource': resource})
