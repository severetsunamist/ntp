# Generated by Django 4.1.7 on 2023-03-13 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='_3pl_offered',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='block',
            name='_3pl_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='celling_height',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='column_grid',
            field=models.CharField(blank=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='block',
            name='commercial_comment',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='block',
            name='docks_amount',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='block',
            name='el_power',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='block',
            name='fire_system_type',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='block',
            name='floor_load',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='floor_type',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='block',
            name='gates_amount',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='block',
            name='heating',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='block',
            name='lease_mez_price',
            field=models.PositiveIntegerField(default=7000),
        ),
        migrations.AlterField(
            model_name='block',
            name='lease_offered',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='lease_office_price',
            field=models.PositiveIntegerField(default=7000),
        ),
        migrations.AlterField(
            model_name='block',
            name='lease_whs_price',
            field=models.PositiveIntegerField(default=7000),
        ),
        migrations.AlterField(
            model_name='block',
            name='mez_area',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='office_area',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='sale_mez_price',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='sale_offered',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='block',
            name='sale_office_price',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='sale_whs_price',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='tech_comment',
            field=models.TextField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='block',
            name='whs_area',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='card',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='listing.companycard'),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='bank_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='bik',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='c_account',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='ceo',
            field=models.CharField(blank=True, max_length=96),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='email',
            field=models.CharField(blank=True, max_length=48),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='inn',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='kpp',
            field=models.CharField(blank=True, max_length=9),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='legal_address',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='legal_name',
            field=models.CharField(blank=True, max_length=96),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='ogrn',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='p_account',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='companycard',
            name='post_address',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='property',
            name='gba',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='gla',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='highway',
            field=models.CharField(choices=[('в черте МКАД', 'в черте МКАД'), ('Алтуфьевское шоссе', 'Алтуфьевское шоссе'), ('Варшавское шоссе', 'Варшавское шоссе'), ('Внуковское шоссе', 'Внуковское шоссе'), ('Дмитровское шоссе', 'Дмитровское шоссе'), ('Каширское шоссе', 'Каширское шоссе'), ('Киевское шоссе', 'Киевское шоссе'), ('Ленинградское шоссе', 'Ленинградское шоссе'), ('Минское шоссе', 'Минское шоссе'), ('Новорязанское шоссе', 'Новорязанское шоссе'), ('Пятницкое шоссе', 'Пятницкое шоссе'), ('Рублёвское шоссе', 'Рублёвское шоссе'), ('Симфиропольское шоссе', 'Симфиропольское шоссе'), ('Шереметьевское шоссе', 'Шереметьевское шоссе'), ('Щёлковское шоссе', 'Щёлковское шоссе'), ('Ярославское шоссе', 'Ярославское шоссе'), ('М4-Дон', 'М4-Дон'), ('М11', 'М11')], default='в черте МКАД', max_length=21),
        ),
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(blank=True, max_length=22),
        ),
        migrations.AlterField(
            model_name='property',
            name='region',
            field=models.CharField(choices=[('Москва', 'Москва'), ('Санкт-Петербург', 'Санкт-Петербург'), ('Казань', 'Казань'), ('Ростов-на-Дону', 'Ростов-на-Дону'), ('Екатеринбург', 'Екатеринбург'), ('Новосибирск', 'Новосибирск'), ('Хабаровск', 'Хабаровск'), ('Владивосток', 'Владивосток')], default='Москва', max_length=15),
        ),
    ]