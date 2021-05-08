from django.conf import settings
from django.db import models


# отделы организации
class Division(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование отдела.')

    # внешние ключи
    head = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='division_head',
                             verbose_name='Глава отдела.')


# сотрудники организации
class Employee(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя сотрудника.')
    last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Фамилия сотрудника.')
    middle_name = models.CharField(max_length=50, blank=False, verbose_name='Отчество сотрудника.')
    email = models.CharField(max_length=100, null=False, blank=False, verbose_name='Электронная почта сотрудника.')

    # внешние ключи
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=False, blank=False,
                                 verbose_name='Отдел сотрудника.')
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, unique=True,
                                   verbose_name='Аккаунт сотрудника')


# объекты доступа
class Facility(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование объекта доступа.')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=False,
                                      verbose_name='Дата создания объекта доступа.')
    DNS_address = models.CharField(max_length=100, null=True, blank=False,
                                   verbose_name='DNS-адрес точки доступа к объекту.')

    description = models.CharField(max_length=500, null=True, blank=False, verbose_name='Описание объекта доступа.')
    location = models.CharField(max_length=100, verbose_name='Расположение объекта доступа.')

    # внешние ключи
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=False,
                              related_name='facility_owner',
                              verbose_name='Владелец объекта доступа.')
    admin = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=False,
                              related_name='facility_admin',
                              verbose_name='Администратор объекта доступа.')


# ресурсы доступа
class Resource(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование ресурса.')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=False,
                                      verbose_name='Дата создания ресурса.')
    DNS_address = models.CharField(max_length=100, null=True, blank=False,
                                   verbose_name='DNS-адрес точки доступа к ресурсу.')

    description = models.CharField(max_length=500, null=True, blank=False, verbose_name='Описание ресурса.')

    # внешние ключи
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=False,
                              related_name='resource_owner',
                              verbose_name='Владелец ресурса.')
    admin = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=False,
                              related_name='resource_admin',
                              verbose_name='Администратор ресурса.')
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=False, blank=False,
                                 verbose_name='Владелец ресурса.')


# заявки
class Entry(models.Model):
    # даты
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False,
                                      verbose_name='Дата создания заявки.')
    granted_at = models.DateTimeField(auto_now_add=True, null=False, blank=False,
                                      verbose_name='Дата активации (начала работы) заявки.')
    expired_at = models.DateTimeField(auto_now_add=True, null=False, blank=False,
                                      verbose_name='Дата деактивации (окончания работы) заявки.')

    # субъекты доступа
    executor = models.ForeignKey(Employee, null=False, blank=False, on_delete=models.CASCADE,
                                 related_name='entry_executor',
                                 verbose_name='Исполнитель (сотрудник, получающий доступ).')
    author = models.ForeignKey(Employee, null=False, blank=False, on_delete=models.CASCADE,
                               related_name='entry_author',
                               verbose_name='Создатель заявки.')

    # флаги
    is_confirmed = models.BooleanField(default=False, verbose_name='Статус подтвержденности заявки.')

    resource = models.ForeignKey(Resource, null=False, blank=False, on_delete=models.CASCADE,
                                 verbose_name='Ресурса для предоставления доступа.')
