# Generated by Django 4.2 on 2024-08-23 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0005_record_record_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(verbose_name='Результат')),
                ('diagnose', models.CharField(max_length=250, verbose_name='Диагноз')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.record', verbose_name='Запись')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Диагностика',
                'verbose_name_plural': 'Диагностики',
                'permissions': [('can_view_diagnostics', 'Может просматривать диагностики')],
            },
        ),
    ]
