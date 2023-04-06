# Generated by Django 4.1.7 on 2023-03-22 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0007_company_logist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/dbmediaroot/block/photo'),
        ),
        migrations.AlterField(
            model_name='block',
            name='plan',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/dbmediaroot/block/plan'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/dbmediaroot/company/logo'),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/dbmediaroot/property/photo'),
        ),
        migrations.AlterField(
            model_name='property',
            name='plan',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/dbmediaroot/property/plan'),
        ),
    ]