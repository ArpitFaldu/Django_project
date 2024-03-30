# Generated by Django 5.0.2 on 2024-03-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0017_alter_device_battery_alter_device_frontcamera_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='Battery',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='device',
            name='Storage',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='device',
            name='screen_height',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='device',
            name='screen_width',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='device',
            name='weight',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='generation',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ssd',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='rearCamera',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='refreshRate',
            field=models.CharField(max_length=10),
        ),
    ]
