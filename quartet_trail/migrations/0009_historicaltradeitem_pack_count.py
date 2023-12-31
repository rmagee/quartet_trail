# Generated by Django 2.2.2 on 2019-06-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quartet_trail', '0008_historicaltradeitem_serial_number_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltradeitem',
            name='pack_count',
            field=models.PositiveIntegerField(help_text='The number of items packed into this package (where appropriate).', null=True, verbose_name='Pack Count'),
        ),
    ]
