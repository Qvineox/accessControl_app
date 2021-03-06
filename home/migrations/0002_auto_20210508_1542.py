# Generated by Django 3.0.8 on 2021-05-08 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
        ('accounts', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='account',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='division',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='facility',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='owner',
        ),
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_author', to='accounts.Employee', verbose_name='Создатель заявки.'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_executor', to='accounts.Employee', verbose_name='Исполнитель (сотрудник, получающий доступ).'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Resource', verbose_name='Ресурса для предоставления доступа.'),
        ),
        migrations.DeleteModel(
            name='Division',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Facility',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
    ]
