from django.db import models


# заявки
class Entry(models.Model):
    # даты
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False,
                                      verbose_name='Дата создания')
    granted_at = models.DateTimeField(null=False, blank=False,
                                      verbose_name='Дата активации')
    expired_at = models.DateTimeField(null=False, blank=False,
                                      verbose_name='Дата деактивации')

    # субъекты доступа
    executor = models.ForeignKey('accounts.Employee', null=False, blank=False, on_delete=models.CASCADE,
                                 related_name='entry_executor',
                                 verbose_name='Исполнитель')
    author = models.ForeignKey('accounts.Employee', null=False, blank=False, on_delete=models.CASCADE,
                               related_name='entry_author',
                               verbose_name='Создатель')

    # статус
    PENDING = 'PD'
    APPROVED = 'AP'
    DENIED = 'DN'
    ACTIVE = 'AC'
    EXPIRED = 'EX'
    RECALLED = 'RC'

    STATUS_CHOICES = [
        (PENDING, 'Ожидание'),
        (APPROVED, 'Подтверждено'),
        (DENIED, 'Отказано'),
        (ACTIVE, 'Активно'),
        (RECALLED, 'Отозвано'),
        (EXPIRED, 'Просрочено'),

    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PD', verbose_name='Статус', null=False,
                              blank=False)

    resource = models.ForeignKey('resources.Resource', null=False, blank=False, on_delete=models.CASCADE,
                                 verbose_name='Ресурс')

    def __str__(self):
        return 'ID#{0}'.format(self.id)
