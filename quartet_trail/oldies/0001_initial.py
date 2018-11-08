# Generated by Django 2.1.1 on 2018-11-08 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quartet_masterdata', '0002_auto_20180821_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTradeItem',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('country_of_origin', models.CharField(help_text='Country from which the goods are supplied. The code list for this attribute is the ISO 3166-1 Alpha-2 list of 2-letter country codes', max_length=2, null=True, verbose_name='Country Of Origin')),
                ('drained_weight', models.FloatField(help_text='The weight of the trade item when drained of its liquid. For example 225 grm', null=True, verbose_name='Drained Weight')),
                ('drained_weight_uom', models.CharField(help_text='The unit of measure for the drained weight as defined inUN/ECE Recommendation 20.', max_length=5, null=True, verbose_name='Drained Weight UOM')),
                ('gross_weight', models.FloatField(help_text='Used to identify the gross weight of the trade item. The gross weight includes all packaging materials of the trade item.', null=True, verbose_name='Gross Weight')),
                ('gross_weight_uom', models.CharField(help_text='The unit of measure for the gross weight as defined inUN/ECE Recommendation 20.', max_length=5, null=True, verbose_name='Gross Weight UOM')),
                ('net_weight', models.FloatField(help_text='Used to identify the net weight of the trade item. Net weight excludes any packaging materials and applies to all levels but consumer unit level.', null=True, verbose_name='Net Weight')),
                ('net_weight_uom', models.CharField(help_text='The unit of measure for the net weight as defined inUN/ECE Recommendation 20.', max_length=5, null=True, verbose_name='NET Weight UOM')),
                ('image', models.TextField(help_text='An image to represent the product in a GUI or report.', max_length=100, null=True, verbose_name='Icon')),
                ('GTIN14', models.CharField(db_index=True, help_text='The GS1 GTIN-14 associated with the Trade Item.', max_length=14, verbose_name='GTIN-14')),
                ('NDC', models.CharField(help_text='The national drug code for the product. US Only.', max_length=12, null=True, verbose_name='NDC')),
                ('NDC_pattern', models.CharField(choices=[('4-4-2', '4-4-2'), ('5-3-2', '5-3-2'), ('5-4-1', '5-4-1')], help_text='The pattern of the NDC.  US Only.  Optional.', max_length=5, null=True, verbose_name='NDC_pattern')),
                ('additional_id', models.CharField(help_text='A trade item identifier that is in addition to the GTIN.', max_length=80, null=True, verbose_name='Additional ID')),
                ('additional_id_typecode', models.CharField(help_text='The code list for this attribute is defined in GS1 GDSN.', max_length=250, null=True, verbose_name='Additional ID TypeCode')),
                ('description_short', models.CharField(help_text='A free form short length description of the trade item that can be used to identify the trade item at point of sale.', max_length=35, null=True, verbose_name='description_short')),
                ('dosage_form_type', models.CharField(help_text='A dosage form is the physical form of a medication that identifies the form of the pharmaceutical item. For example: PILL', max_length=35, null=True, verbose_name='Dosage Form Type')),
                ('functional_name', models.CharField(help_text='Describes use of the product or service by the consumer. Should help clarify the product classification associated with the GTIN.', max_length=100, null=True, verbose_name='functional_name')),
                ('manufacturer_name', models.CharField(help_text='Party name information for the manufacturer of the trade item. Example: Acme Corporation', max_length=300, null=True, verbose_name='manufacturer_name')),
                ('net_content_description', models.CharField(help_text='Free text describing the amount of the trade item contained by a package, usually as claimed on the label. Example: 253 grams', max_length=500, null=True, verbose_name='Net Content Description')),
                ('label_description', models.CharField(help_text="A literal reproduction of the text featured on a product's label in the same word-by-word order in which it appears on the front of the product's packaging.", max_length=500, null=True, verbose_name='Label Description')),
                ('regulated_product_name', models.CharField(help_text='The prescribed, regulated or generic product name or denomination that describes the true nature of the product according to country specific regulation.', max_length=500, null=True, verbose_name='regulated_product_name')),
                ('strength_description', models.CharField(help_text='Free text describing the strength of the active ingredient(s) of the product. Example: 200mg/100mg', max_length=500, null=True, verbose_name='strength_description')),
                ('trade_item_description', models.CharField(help_text='An understandable and useable description of a trade item using brand and other descriptors.', max_length=200, null=True, verbose_name='Trade Item Description')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('company', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_masterdata.Company')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Trade Item',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='TrailEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('user_id', models.BigIntegerField(blank=True, db_index=True)),
                ('data', models.TextField(blank=True)),
                ('action', models.CharField(blank=True, max_length=16)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
            options={
                'db_table': 'trail_entry',
            },
        ),
    ]