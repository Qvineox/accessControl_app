from django.conf import settings
from django.db import models


# отделы организации
class Division(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', null=False, blank=False)

    # внешние ключи
    head = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='division_head',
                             verbose_name='Глава', null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.name)


# сотрудники организации
class Employee(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='Электронная почта')

    # внешние ключи
    division = models.ForeignKey('Division', on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name='Отдел')
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                   unique=True,
                                   verbose_name='Аккаунт')

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)
