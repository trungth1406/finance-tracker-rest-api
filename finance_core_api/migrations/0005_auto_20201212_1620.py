# Generated by Django 3.1.3 on 2020-12-12 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_core_api', '0004_resource_remain_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='current_amount',
            new_name='total_amount',
        ),
    ]