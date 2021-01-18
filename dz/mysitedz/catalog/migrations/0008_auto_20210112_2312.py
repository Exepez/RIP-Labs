# Generated by Django 3.1.4 on 2021-01-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210112_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='description',
            field=models.TextField(help_text='Введите описание', max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='manufacturer_img',
            field=models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='urlman',
            field=models.URLField(help_text='Введите URL', null=True, verbose_name='URL'),
        ),
    ]
