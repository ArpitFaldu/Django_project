# Generated by Django 5.0.2 on 2024-03-30 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0018_alter_device_battery_alter_device_storage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='Battery',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='device',
            name='Storage',
            field=models.IntegerField(max_length=10),
        ),
    ]
