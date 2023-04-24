# Generated by Django 4.1.7 on 2023-03-29 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0017_block_floor_level_block_lease_avg_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='celling_height',
            field=models.PositiveSmallIntegerField(blank=True, default=12, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='docks_amount',
            field=models.PositiveSmallIntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='el_power',
            field=models.CharField(blank=True, default='200 кВт', max_length=8),
        ),
        migrations.AlterField(
            model_name='block',
            name='fire_system_type',
            field=models.CharField(choices=[('Спринклерная система', 'Спринклерная система'), ('Гидранты', 'Гидранты'), ('Огнетушители', 'Огнетушители'), ('Порошковая система', 'Порошковая система'), ('Специальная система', 'Специальная система'), ('Нет', 'Нет')], default='Спринклерная система пожаротушения', max_length=20),
        ),
        migrations.AlterField(
            model_name='block',
            name='floor_level',
            field=models.FloatField(blank=True, default=1.2, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='floor_load',
            field=models.PositiveSmallIntegerField(blank=True, default=8, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='gates_amount',
            field=models.PositiveSmallIntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='heating',
            field=models.CharField(choices=[('Центральное отопление', 'Центральное отопление'), ('Собственная котельная', 'Собственная котельная'), ('Электрическое отопление', 'Электрическое отопление'), ('Воздушное отопление', 'Воздушное отопление'), ('Тёплый пол', 'Тёплый пол'), ('Нет', 'Нет')], default='Центральное отопление', max_length=23),
        ),
        migrations.AlterField(
            model_name='block',
            name='lease_avg_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='lease_mez_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='lease_offered',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='lease_office_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='lease_total_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='lease_whs_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='log_offered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='block',
            name='mez_area',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='block',
            name='office_area',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='block',
            name='opex',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='sale_avg_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='sale_mez_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='sale_office_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='sale_total_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='sale_whs_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='temp_cond_max',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='temp_cond_min',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='total_area',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='block',
            name='whs_area',
            field=models.PositiveIntegerField(),
        ),
    ]