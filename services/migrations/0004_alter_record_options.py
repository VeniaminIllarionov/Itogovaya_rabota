# Generated by Django 4.2 on 2024-08-23 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_record'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'permissions': [('can_add_record', 'Может добавлять запись'), ('can_change_record', 'Может изменять запись'), ('can_view_record', 'Может просматривать запись'), ('can_delete_record', 'Может удалять запись')], 'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
    ]
