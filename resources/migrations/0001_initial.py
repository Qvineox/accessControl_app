# Generated by Django 3.0.8 on 2021-05-08 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование объекта доступа.')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания объекта доступа.')),
                ('DNS_address', models.CharField(max_length=100, null=True, verbose_name='DNS-адрес точки доступа к объекту.')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='Описание объекта доступа.')),
                ('location', models.CharField(max_length=100, verbose_name='Расположение объекта доступа.')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='facility_admin', to='accounts.Employee', verbose_name='Администратор объекта доступа.')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facility_owner', to='accounts.Employee', verbose_name='Владелец объекта доступа.')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование ресурса.')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания ресурса.')),
                ('DNS_address', models.CharField(max_length=100, null=True, verbose_name='DNS-адрес точки доступа к ресурсу.')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='Описание ресурса.')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resource_admin', to='accounts.Employee', verbose_name='Администратор ресурса.')),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Facility', verbose_name='Владелец ресурса.')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource_owner', to='accounts.Employee', verbose_name='Владелец ресурса.')),
            ],
        ),
    ]
