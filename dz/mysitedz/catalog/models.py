from django.db import models
import datetime

# Create your models here.
class CPU(models.Model):

    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    
    

    name = models.CharField('Название процессора', max_length=50, help_text="Введите название процессора")
    price = models.CharField('Цена процессора', max_length=20,  null=True, help_text="Введите цену процессора")

    generation = models.CharField('Поколение процессора', max_length=50, null=True, help_text="Введите поколение процессора")
    yearrelease = models.IntegerField('Год релиза', choices=YEAR_CHOICES, null=True, help_text="Выберите год релиза процессора")
    socket = models.CharField('Сокет',max_length=20,  help_text="Введите сокет")

    numcore = models.IntegerField('Количество ядер', null=True,help_text="Введите количество ядер")
    numstream = models.IntegerField('Количество потоков', null=True,help_text="Введите количество потоков")
    cacheL1 = models.CharField('Кэш L1',max_length=20, null=True, help_text="Введите объем кэша L1")    
    cacheL2 = models.CharField('Кэш L2',max_length=20, null=True, help_text="Введите объем кэша L2")   
    cacheL3 = models.CharField('Кэш L3',max_length=20, null=True, help_text="Введите объем кэша L3") 

    basefreq = models.CharField('Базовая частота процессора',max_length=20, null=True, help_text="Введите базовую частоту процессора")
    maxfreq = models.CharField('Максимальная частота процессора',max_length=20, null=True, help_text="Введите максимальную частоту процессора")
    countrate = models.IntegerField('Количество оценок',null=True)
    rate = models.IntegerField('Общая оценка',null=True)
    avrrate = models.FloatField('Средняя оценка',null=True)


    cpu_img = models.ImageField('Изображение',upload_to='images/', blank=True, null=True, help_text="Загрузите изображение")

    def get_absolute_url(self):
        return reverse('cpu-detail', args=[str(self.id)])

    def __str__(self):
          return '%s, %s' % (self.name, self.socket)

    @property
    def cpu_img_url(self):
        if self.cpu_img and hasattr(self.cpu_img, 'url'):
            return self.cpu_img.url
    
    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'


class Manufacturer(models.Model):

    
    namecompany = models.CharField('Название производителя', max_length=100, help_text="Введите название производителя")
    description = models.TextField('Описание',max_length=1000, null=True, help_text="Введите описание")
    urlman = models.URLField('URL', null=True, help_text="Введите URL")
    manufacturer_img = models.ImageField('Изображение',upload_to='images/', blank=True, null=True, help_text="Загрузите изображение (рекомендуется 1200x300)")
    
    def get_absolute_url(self):
        return reverse('manufacturer-detail', args=[str(self.id)])

    def __str__(self):
        return self.namecompany

    @property
    def manufacturer_img_url(self):
        if self.manufacturer_img and hasattr(self.manufacturer_img, 'url'):
            return self.manufacturer_img.url
    
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'



from django.urls import reverse

class Motherboard(models.Model):

    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    title = models.CharField('Название материнской платы', max_length=50, help_text="Введите название материнской платы")
    price = models.CharField('Цена материнской платы', max_length=20, null=True, help_text="Введите цену материнской платы")
    yearrelease = models.IntegerField('Год релиза', choices=YEAR_CHOICES, null=True, help_text="Выберите год релиза материнской платы")
    formfactor = models.CharField('Форм-фактор',max_length=50, help_text="Введите форм фактор")
    typememory = models.CharField('Тип памяти',max_length=20, help_text="Введите тип памяти")
    socket = models.CharField('Сокет',max_length=20,  help_text="Введите сокет")
    countrate = models.IntegerField('Количество оценок',null=True)
    rate = models.IntegerField('Общая оценка',null=True)
    avrrate = models.FloatField('Средняя оценка',null=True)

    motherboard_img = models.ImageField('Изображение',upload_to='images/', blank=True, null=True, help_text="Загрузите изображение")

    cpu = models.ManyToManyField(CPU, help_text="Выберите подходящий процессор", verbose_name='Подходящие процессоры')
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True, verbose_name='Производитель')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('motherboard-detail', args=[str(self.id)])
    
    @property
    def motherboard_img_url(self):
        if self.motherboard_img and hasattr(self.motherboard_img, 'url'):
            return self.motherboard_img.url
    
    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнские платы'



# class Person(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()


# class ReviewCPU(models.Model):
#     RATE_CHOICES = []
#     for r in range(0, 6):
#         RATE_CHOICES.append((r,r))
#     comment = models.TextField('Отзыв',max_length=1000, null=True, help_text="Введите отзыв")
#     rate = models.IntegerField('Оценка', choices=RATE_CHOICES, null=True, help_text="Оцените товар")
#     cpu = models.ForeignKey('CPU', on_delete=models.SET_NULL, null=True)

#     def get_absolute_url(self):
#         return reverse('reviewcpu-detail', args=[str(self.id)])

#     def __str__(self):
#         return self.comment



