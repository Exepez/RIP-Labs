# Generated by Django 3.1.4 on 2021-01-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_auto_20210113_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='countrate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='rate',
            field=models.IntegerField(null=True),
        ),
    ]
