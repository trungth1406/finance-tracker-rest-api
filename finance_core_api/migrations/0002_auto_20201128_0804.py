# Generated by Django 3.1.3 on 2020-11-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_core_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='resource',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
