# Generated by Django 3.1.4 on 2021-01-11 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название процессора', max_length=50, verbose_name='Название процессора')),
                ('numcore', models.IntegerField(help_text='Введите количество ядер', verbose_name='Количество ядер')),
                ('numstream', models.IntegerField(help_text='Введите количество потоков', verbose_name='Количество потоков')),
                ('freq', models.CharField(help_text='Введите частоту процессора', max_length=20, verbose_name='Частота процессора')),
                ('socket', models.CharField(help_text='Введите сокет', max_length=20, verbose_name='Сокет')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namecompany', models.CharField(help_text='Введите название производителя', max_length=100, verbose_name='Название производителя')),
            ],
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название материнской платы', max_length=50, verbose_name='Название материнской платы')),
                ('typememory', models.CharField(help_text='Введите тип памяти', max_length=20, verbose_name='Тип памяти')),
                ('formfactor', models.CharField(help_text='Введите форм фактор', max_length=50, verbose_name='Форм-фактор')),
                ('socket', models.CharField(help_text='Введите сокет', max_length=20, verbose_name='Сокет')),
                ('cpu', models.ManyToManyField(help_text='Выберите подходящий процессор', to='catalog.CPU')),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.manufacturer')),
            ],
        ),
    ]
