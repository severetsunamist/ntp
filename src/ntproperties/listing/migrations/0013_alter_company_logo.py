# Generated by Django 4.1.7 on 2023-03-22 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0012_alter_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]