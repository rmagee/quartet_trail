# Generated by Django 2.2 on 2019-05-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quartet_trail', '0007_auto_20190305_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltradeitem',
            name='serial_number_length',
            field=models.PositiveSmallIntegerField(help_text="The length of this material's serial number field", null=True, verbose_name='Serial Number Length'),
        ),
    ]