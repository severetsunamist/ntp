# Generated by Django 4.1.7 on 2023-03-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0010_alter_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='block',
            name='plan',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='property',
            name='plan',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]