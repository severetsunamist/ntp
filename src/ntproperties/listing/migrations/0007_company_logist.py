# Generated by Django 4.1.7 on 2023-03-22 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0006_rename_tenant_company_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logist',
            field=models.BooleanField(default=False),
        ),
    ]