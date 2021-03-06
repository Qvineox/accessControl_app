# Generated by Django 3.0.8 on 2021-05-08 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210508_2014'),
        ('resources', '0003_auto_20210508_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='DNS_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='DNS-адрес точки доступа'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='facility_admin', to='accounts.Employee', verbose_name='Администратор'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Расположение'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='DNS_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='DNS-адрес точки доступа'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resource_admin', to='accounts.Employee', verbose_name='Администратор'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
    ]
