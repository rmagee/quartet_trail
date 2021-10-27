# Generated by Django 3.0.5 on 2020-08-24 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quartet_trail', '0017_auto_20200401_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalauthenticationinfo',
            name='description',
            field=models.CharField(blank=True, help_text='An optional description.', max_length=200, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='historicalauthenticationinfo',
            name='private_key',
            field=models.TextField(blank=True, help_text='Any private key value if applicable.', null=True, verbose_name='Private Key'),
        ),
        migrations.AlterField(
            model_name='historicalauthenticationinfo',
            name='public_key',
            field=models.TextField(blank=True, help_text='Any public key info if applicable.', null=True, verbose_name='Public Key'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='action',
            field=models.CharField(blank=True, choices=[('ADD', 'Add'), ('OBSERVE', 'Observe'), ('DELETE', 'Delete')], help_text="The EPCIS event's ACTION type.", max_length=20, null=True, verbose_name='Action'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='biz_location',
            field=models.CharField(blank=True, help_text='The business location URN.  Typically representing a site', max_length=150, null=True, verbose_name='Business Location'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='biz_step',
            field=models.CharField(blank=True, help_text='The business step URN.  Can be a CBV value or any customuri.  If CBV it must be exactly as specified in v1.2', max_length=150, null=True, verbose_name='Business Step (BizStep)'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='destination_id',
            field=models.CharField(blank=True, help_text='A URI that identifies the Destination specified in the Destination Type field.', max_length=200, null=True, verbose_name='Destination ID'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='destination_type',
            field=models.CharField(blank=True, help_text='The type of the Destination- a CBV 1.2 URI or custom URI.', max_length=150, null=True, verbose_name='Destination Type'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='disposition',
            field=models.CharField(blank=True, help_text='A Disposition URN- can be CBV or custom.', max_length=150, null=True, verbose_name='Disposition'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='event_type',
            field=models.CharField(blank=True, choices=[('Object', 'Object'), ('Transaction', 'Transaction'), ('Transformation', 'Transformation'), ('Aggregation', 'Aggregation')], help_text='The type of EPCIS event.', max_length=20, null=True, verbose_name='Event Type'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='read_point',
            field=models.CharField(blank=True, help_text='The read point URN.  Typically representing a sub-site.', max_length=150, null=True, verbose_name='Read Point'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='receiver_identifier',
            field=models.CharField(blank=True, help_text='Typically an SGLN but an identifier that is in the SBDH and uniquely identifies a receiving entity.', max_length=250, null=True, verbose_name='SBDH Receiver Identifier'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='sender_identifier',
            field=models.CharField(blank=True, help_text='Typically an SGLN but an identifier that is in the SBDH and uniquely identifies a sending entity.', max_length=250, null=True, verbose_name='SBDH Sender Identifier'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='source_id',
            field=models.CharField(blank=True, help_text='A URI that identifies the source specified in the Source Type field.', max_length=200, null=True, verbose_name='Source ID'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='source_type',
            field=models.CharField(blank=True, help_text='The type of the source- a CBV 1.2 URI or custom URI.', max_length=150, null=True, verbose_name='Source Type'),
        ),
    ]
