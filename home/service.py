from accounts.models import Employee
from django.utils import timezone
from resources.models import Resource

from .models import *


def get_all_entries():
    items = Entry.objects.filter().order_by('status', '-expired_at')
    return items


def get_expired_entries(items):
    for entry in items:
        if entry.status != entry.RECALLED and entry.expired_at < timezone.now():
            entry.status = entry.EXPIRED

    return items


def get_entry(entry_id):
    item = Entry.objects.get(id=entry_id)
    if item.status != item.RECALLED and item.expired_at < timezone.now():
        item.status = item.EXPIRED

    return item


def get_all_employees():
    items = Employee.objects.filter().order_by('last_name')
    return items


def get_all_resources():
    items = Resource.objects.filter().order_by('facility')
    return items
