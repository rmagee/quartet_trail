# Generated by Django 2.1.5 on 2019-03-05 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quartet_trail', '0006_auto_20190214_1807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalcompany',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Company'},
        ),
        migrations.AlterModelOptions(
            name='historicaltemplate',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Template'},
        ),
    ]
