# Generated by Django 3.1.3 on 2020-11-29 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance_core_api', '0002_auto_20201128_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='fk_resource',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance_core_api.resource'),
        ),
    ]
