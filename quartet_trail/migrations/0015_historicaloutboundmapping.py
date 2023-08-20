# Generated by Django 3.0.2 on 2020-02-12 16:50

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('quartet_masterdata', '0008_outboundmapping'),
        ('quartet_trail', '0014_auto_20191219_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalOutboundMapping',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_user_id', models.CharField(max_length=200, null=True, verbose_name='username')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('company', models.ForeignKey(blank=True, db_constraint=False, help_text='The company to create the trading partner mapping for', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_masterdata.Company', verbose_name='Company')),
                ('from_business', models.ForeignKey(blank=True, db_constraint=False, help_text='The default from company to use if the company is not used in the mapping.  Leave this blank if the company is always the business owner for outbound master data.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_masterdata.Company', verbose_name='Default From')),
                ('ship_from', models.ForeignKey(blank=True, db_constraint=False, help_text='The default ship from location for the company.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_masterdata.Location', verbose_name='Default Ship From')),
                ('ship_to', models.ForeignKey(blank=True, db_constraint=False, help_text='The default ship to location for the company.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_masterdata.Location', verbose_name='Default Ship To')),
                ('to_business', models.ForeignKey(blank=True, db_constraint=False, help_text='The default to which product shipments will be mapped if applicable.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_masterdata.Company', verbose_name='Default To Business')),
            ],
            options={
                'verbose_name': 'historical outbound mapping',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]