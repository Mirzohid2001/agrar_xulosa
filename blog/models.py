from django.db import models
from django.db.models import CASCADE


# Create your models here.
# 1. Yillik ish kuni nima ? Tractorga field qilib qo'shish kerakmi ?


REGION = (
    ('1-MINTAQA', '1-MINTAQA'),
    ('2-MINTAQA', '2-MINTAQA'),
    ('3-MINTAQA', '3-MINTAQA'),
)

class Region(models.Model):
    name = models.CharField(max_length=255, choices=REGION)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Tractor(models.Model):
    place = models.ForeignKey(Region,on_delete=models.CASCADE,related_name='tractors')
    model = models.CharField(max_length=255)
    marka = models.CharField(max_length=255)
    price_a_hectare = models.FloatField()
    price_a_moto = models.FloatField()
    year = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Worker(models.Model):
    name = models.CharField(max_length=255)
    salary = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'




class WorkType(models.Model):
    place = models.ForeignKey(Region,on_delete=models.CASCADE,related_name='work_types')
    name = models.CharField(max_length=255)
    tractor = models.ForeignKey('blog.Tractor', CASCADE, 'work_types')
    worker = models.ForeignKey('blog.Worker', CASCADE, 'work_types')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип работы'
        verbose_name_plural = 'Типы работы'



class Order(models.Model):
    tractor = models.ForeignKey('blog.Tractor', CASCADE, 'orders')
    work_type = models.ForeignKey('blog.WorkType', CASCADE, 'orders')
    area = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # start_date = models.DateField() # So'rayman ABS akadan
    # end_date = models.DateField()

    def __str__(self):
        return str(self.tractor, self.area)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Seed(models.Model):
    place = models.ForeignKey(Region,on_delete=models.CASCADE,related_name='seeds')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    volume = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Семя'
        verbose_name_plural = 'Семена'





class Fertiliser(models.Model):
    place = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='fertilisers')
    azot_kg = models.FloatField()
    price_azot = models.FloatField()
    soil_azot = models.FloatField()
    soil_azot_price = models.FloatField()
    fosfor_kaliy_azotN = models.FloatField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Удобрение'
        verbose_name_plural = 'Удобрения'

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'













