from collections import defaultdict
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import *
from .service import *


# Create your views here.

def dashboard(request):
    return render(request, 'home/dashboard.html')


def entries_view(request):
    entries = get_expired_entries(get_all_entries())
    return render(request, 'home/all_entries.html', {'entries': entries})


def entry_view(request, entry_id):
    entry = get_entry(entry_id)

    if request.method == 'POST':
        if request.POST['action']:
            if request.POST['action'] == 'recall':
                entry.status = entry.RECALLED
                entry.save()
            elif request.POST['action'] == 'activate':
                entry.status = entry.ACTIVE
                entry.save()

    entry.duration = entry.expired_at - entry.granted_at

    return render(request, 'home/entry_page.html', {'entry': entry})


def add_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['expired_at'] < form.cleaned_data['granted_at']:
                messages.warning(request, 'Дата конца действия не должна быть раньше начала!')
            else:
                new_entry = Entry.objects.create(created_at=timezone.now(),
                                                 granted_at=form.cleaned_data['granted_at'],
                                                 expired_at=form.cleaned_data['expired_at'],
                                                 executor=Employee.objects.get(id=form.cleaned_data['executor']),
                                                 author=Employee.objects.get(id=form.cleaned_data['author']),
                                                 resource=Resource.objects.get(id=form.cleaned_data['resource']),
                                                 status=form.cleaned_data['status'])
                new_entry.save()
                return redirect('entries')

    employees = get_all_employees()
    resources = get_all_resources()

    return render(request, 'home/entry_editor.html', {'current_time': timezone.now(),
                                                      'employees': employees,
                                                      'resources': resources})
