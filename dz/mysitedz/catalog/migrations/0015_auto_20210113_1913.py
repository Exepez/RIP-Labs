# Generated by Django 3.1.4 on 2021-01-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20210113_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='countrate',
            field=models.IntegerField(default=100, null=True),
        ),
    ]
