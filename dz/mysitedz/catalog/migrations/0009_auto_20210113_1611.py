# Generated by Django 3.1.4 on 2021-01-13 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20210112_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='manufacturer_img',
            field=models.ImageField(blank=True, help_text='Загрузите изображение (рекомендуется 1200x300)', null=True, upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='ReviewCPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(help_text='Введите отзыв', max_length=1000, null=True, verbose_name='Отзыв')),
                ('rate', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], help_text='Оцените товар', null=True, verbose_name='Оценка')),
                ('cpu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.cpu')),
            ],
        ),
    ]
