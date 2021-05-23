from accounts.models import Employee
from datetime import datetime
from django.db.models import Q
from django.utils import timezone
from django.utils.timezone import make_aware
from resources.models import Resource

from .models import *

from accounts.service import *
from resources.service import *


def get_all_entries():
    items = Entry.objects.filter().order_by('status', '-expired_at')
    return items


def get_entries_realtime_status(items):
    for _ in items:
        if _.status != Entry.RECALLED and _.status != Entry.PENDING and _.granted_at <= timezone.now():
            if _.expired_at >= timezone.now():
                _.status = Entry.ACTIVE
            else:
                _.status = Entry.EXPIRED

    return items


def get_entry(entry_id):
    item = Entry.objects.get(id=entry_id)
    if item.status != item.RECALLED and item.expired_at < timezone.now():
        item.status = item.EXPIRED

    return item


def get_dashboard_entries():
    items = Entry.objects.filter(status__in=[Entry.PENDING, Entry.APPROVED, Entry.EXPIRED, Entry.ACTIVE]).order_by(
        'status', '-expired_at')

    return items


def get_entries_by_filter(parameters):
    parameters['expired_at'] = make_aware(datetime.strptime(parameters['expired_at'], '%Y-%m-%dT%H:%M'))
    parameters['granted_at'] = make_aware(datetime.strptime(parameters['granted_at'], '%Y-%m-%dT%H:%M'))

    query = Entry.objects.filter(expired_at__lte=parameters['expired_at'],
                                 expired_at__gte=parameters['granted_at']) | Entry.objects.filter(
        granted_at__lte=parameters['expired_at'], granted_at__gte=parameters['granted_at']) | Entry.objects.filter(
        granted_at__lte=parameters['granted_at'], expired_at__gte=parameters['expired_at'])

    if len(parameters['executor']) > 0:
        query = query.filter(executor=parameters['executor'])

    if len(parameters['author']) > 0:
        query = query.filter(author=parameters['author'])

    if len(parameters['resource']) > 0:
        query = query.filter(resource=parameters['resource'])

    query = query.order_by('expired_at')

    return query
