from django.db.models import Max
from home.models import Entry

from .models import *


def get_all_resources():
    items = Resource.objects.filter().order_by('facility', 'id')
    return items


def get_all_facilities():
    items = Facility.objects.filter()
    return items


def ger_resource(resource_id):
    item = Resource.objects.get(id=resource_id)

    # получение данных по последнем получении доступа к данному ресурсу
    latest_access = Entry.objects.filter(resource_id=resource_id).aggregate(Max('expired_at'))['expired_at__max']
    item.latest_access = latest_access

    return item
