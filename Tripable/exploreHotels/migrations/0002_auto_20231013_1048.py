# Generated by Django 3.2.19 on 2023-10-13 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exploreHotels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='ac_rooms',
        ),
        migrations.RemoveField(
            model_name='hotels',
            name='price',
        ),
        migrations.RemoveField(
            model_name='hotels',
            name='rooms',
        ),
        migrations.AddField(
            model_name='hotels',
            name='facilityoftype1',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='hotels',
            name='facilityoftype2',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='hotels',
            name='facilityoftype3',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='hotels',
            name='pricetype1',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='hotels',
            name='pricetype2',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='hotels',
            name='pricetype3',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='hotels',
            name='roomtype1',
            field=models.CharField(default='Regular', max_length=100),
        ),
        migrations.AddField(
            model_name='hotels',
            name='roomtype2',
            field=models.CharField(default='Regular', max_length=100),
        ),
        migrations.AddField(
            model_name='hotels',
            name='roomtype3',
            field=models.CharField(default='Regular', max_length=100),
        ),
    ]