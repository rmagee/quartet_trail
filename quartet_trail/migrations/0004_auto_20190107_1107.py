# Generated by Django 2.1.5 on 2019-01-07 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quartet_trail', '0003_auto_20181225_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalcompany',
            name='company_type',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Describes the type of company.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_masterdata.CompanyType', verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='authentication_info',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The Authentication Info to use.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_output.AuthenticationInfo', verbose_name='Authentication Info'),
        ),
        migrations.AlterField(
            model_name='historicalepcisoutputcriteria',
            name='end_point',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='A prtocol-specific endpoint defining where any output data will be sent.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_output.EndPoint', verbose_name='End Point'),
        ),
        migrations.AlterField(
            model_name='historicallistbasedregion',
            name='authentication_info',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The Authentication Info to use.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_output.AuthenticationInfo', verbose_name='Authentication Info'),
        ),
        migrations.AlterField(
            model_name='historicallistbasedregion',
            name='end_point',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='A protocol-specific endpoint defining whereany data will come from', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_output.EndPoint', verbose_name='End Point'),
        ),
        migrations.AlterField(
            model_name='historicallistbasedregion',
            name='pool',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The Number Pool this region will belong to.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='serialbox.Pool', verbose_name='Number Pool'),
        ),
        migrations.AlterField(
            model_name='historicallistbasedregion',
            name='rule',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='A rule that may be executed by the region processing class.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_capture.Rule', verbose_name='Processing Rule'),
        ),
        migrations.AlterField(
            model_name='historicallistbasedregion',
            name='template',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The Django/Jinja template to send a formatted request for number ranges', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_templates.Template', verbose_name='Message Template'),
        ),
        migrations.AlterField(
            model_name='historicallocation',
            name='company',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The company, if any, associated with this location.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_masterdata.Company', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='historicallocation',
            name='location_type',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='An additional classifier that can be used to identifythe location outside of the CBV codes.  This can be an internal classifier or a human readable that lends further clarity to the location record.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_masterdata.LocationType', verbose_name='Location Type'),
        ),
        migrations.AlterField(
            model_name='historicallocation',
            name='site',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Identifies the site in which this location is contained...if at all. For a Sub-site location, this is the identifier of the parent location.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_masterdata.Location', verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='historicalprocessingparameters',
            name='list_based_region',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='A key-value pair object meant to hold parameters used for processing classes.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='list_based_flavorpack.ListBasedRegion', verbose_name='Processing Class Parameter'),
        ),
        migrations.AlterField(
            model_name='historicalrandomizedregion',
            name='pool',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The Number Pool this region will belong to.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='serialbox.Pool', verbose_name='Number Pool'),
        ),
        migrations.AlterField(
            model_name='historicalresponserule',
            name='pool',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The Pool to associate this response configuration with.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='serialbox.Pool', verbose_name='Pool'),
        ),
        migrations.AlterField(
            model_name='historicalresponserule',
            name='rule',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The rule to execute during response generation.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_capture.Rule'),
        ),
        migrations.AlterField(
            model_name='historicalresponsetemplate_pool',
            name='pool',
            field=models.ForeignKey(blank=True, db_constraint=False, db_tablespace='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='serialbox.Pool'),
        ),
        migrations.AlterField(
            model_name='historicalresponsetemplate_pool',
            name='responsetemplate',
            field=models.ForeignKey(blank=True, db_constraint=False, db_tablespace='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='serialbox.ResponseTemplate'),
        ),
        migrations.AlterField(
            model_name='historicalrulefilter',
            name='filter',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The filter to associate this search value with.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_capture.Filter', verbose_name='Filter'),
        ),
        migrations.AlterField(
            model_name='historicalrulefilter',
            name='rule',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The rule to execute if the search term executes.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_capture.Rule', verbose_name='Rule'),
        ),
        migrations.AlterField(
            model_name='historicalruleparameter',
            name='rule',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text="A parameter associted with a given rule.  Each parameter is passed into the Rule as a dictionary entrance in the rule's context.", null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_capture.Rule', verbose_name='Rule Field'),
        ),
        migrations.AlterField(
            model_name='historicalsequentialregion',
            name='pool',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The Number Pool this region will belong to.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='serialbox.Pool', verbose_name='Number Pool'),
        ),
        migrations.AlterField(
            model_name='historicalstep',
            name='rule',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The parent rule.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_capture.Rule', verbose_name='Rule'),
        ),
        migrations.AlterField(
            model_name='historicalstepparameter',
            name='step',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='A field associted with a given step.  Fields are passed into Step instances when they are dynamically created as variables.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_capture.Step', verbose_name='Step Field'),
        ),
        migrations.AlterField(
            model_name='historicaltaskparameter',
            name='task',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='A field associted with a given task.  Fields are passed into task instances when they are dynamically created as variables.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_capture.Task', verbose_name='Task'),
        ),
        migrations.AlterField(
            model_name='historicaltradeitem',
            name='company',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The company, associated with this trade item.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_masterdata.Company', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='historicaltradeitemfield',
            name='trade_item',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The Related Trade Item', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='quartet_masterdata.TradeItem', verbose_name='Trade Item'),
        ),
    ]
