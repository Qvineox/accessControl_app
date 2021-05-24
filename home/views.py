from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import *
from .service import *


# Create your views here.

def dashboard(request):
    entries = get_entries_realtime_status(get_dashboard_entries())

    active = []
    pending = []
    expired = []
    approved = []

    for entry in entries:
        if entry.status == Entry.ACTIVE:
            active.append(entry)
        elif entry.status == Entry.PENDING:
            pending.append(entry)
        elif entry.status == Entry.EXPIRED:
            expired.append(entry)
        elif entry.status == Entry.APPROVED:
            approved.append(entry)

    dashboard_entries = {
        'active': active,
        'pending': pending,
        'expired': expired,
        'approved': approved,
    }

    return render(request, 'home/dashboard.html', {'dashboard_entries': dashboard_entries})


def entries_view(request):
    sorted_entries = {
        'AC': [],
        'PD': [],
        'EX': [],
        'AP': [],
        'RC': [],
    }

    for entry in get_entries_realtime_status(get_all_entries()):
        sorted_entries[entry.status].append(entry)

    return render(request, 'home/all_entries.html', {'entries': sorted_entries})


def entry_view(request, entry_id):
    entry = get_entry(entry_id)

    if request.method == 'POST':
        if request.POST['action']:
            if request.POST['action'] == 'recall':
                entry.status = entry.RECALLED
                entry.save()
            elif request.POST['action'] == 'activate':
                entry.status = entry.APPROVED
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
        else:
            if not hasattr(request.user, 'employee'):
                messages.warning(request, 'Сначала нужно создать работника для своей учетной записи!')

    employees = get_all_employees()
    resources = get_all_resources()

    return render(request, 'home/entry_editor.html', {'current_time': timezone.now(),
                                                      'employees': employees,
                                                      'resources': resources})


def filter_entries(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['expired_at'] < form.cleaned_data['granted_at']:
                messages.warning(request, 'Дата конца выборки не должна быть раньше начала!')
            else:
                print(form.cleaned_data)
                entries = get_entries_by_filter(form.cleaned_data)

                return render(request, 'home/filtered_entries.html', {'entries': entries})

    employees = get_all_employees()
    resources = get_all_resources()

    return render(request, 'home/entry_filter.html', {'employees': employees,
                                                      'resources': resources})
