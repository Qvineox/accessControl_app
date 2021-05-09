from django.db import models


# объекты доступа
class Facility(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=False,
                                      verbose_name='Дата создания')
    DNS_address = models.CharField(max_length=100, null=True, blank=True,
                                   verbose_name='DNS-адрес точки доступа')

    description = models.CharField(max_length=500, null=True, blank=True, verbose_name='Описание')
    location = models.CharField(max_length=100, verbose_name='Расположение', null=True, blank=True)

    # внешние ключи
    owner = models.ForeignKey('accounts.Employee', on_delete=models.CASCADE, null=False, blank=False,
                              related_name='facility_owner',
                              verbose_name='Владелец')
    admin = models.ForeignKey('accounts.Employee', on_delete=models.CASCADE, null=True, blank=True,
                              related_name='facility_admin',
                              verbose_name='Администратор')

    def __str__(self):
        return '{0}'.format(self.name)


# ресурсы доступа
class Resource(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=False,
                                      verbose_name='Дата создания')
    DNS_address = models.CharField(max_length=100, null=True, blank=True,
                                   verbose_name='DNS-адрес точки доступа')

    description = models.CharField(max_length=500, null=True, blank=True, verbose_name='Описание')

    # внешние ключи
    owner = models.ForeignKey('accounts.Employee', on_delete=models.CASCADE, null=False, blank=False,
                              related_name='resource_owner',
                              verbose_name='Владелец')
    admin = models.ForeignKey('accounts.Employee', on_delete=models.CASCADE, null=True, blank=True,
                              related_name='resource_admin',
                              verbose_name='Администратор')
    facility = models.ForeignKey('Facility', on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name='Объект доступа')

    def __str__(self):
        return '{0}'.format(self.name)
