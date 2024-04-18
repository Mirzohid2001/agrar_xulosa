from django.db import models

from users.models import User

REVIEW_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

class Oil(models.Model):
    place = models.ForeignKey(Region, on_delete=models.CASCADE)
    litr = models.CharField(max_length=255)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.litr

class Tractor(models.Model):
    place = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='tractors')
    model = models.CharField(max_length=255)
    marka = models.CharField(max_length=255)
    oil = models.ForeignKey(Oil, on_delete=models.CASCADE, related_name='tractors')
    price_a_hectare = models.FloatField()
    price_a_moto = models.FloatField()
    year = models.DateField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Трактор'
        verbose_name_plural = 'Тракторы'

class Worker(models.Model):
    salary = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

class WorkType(models.Model):
    place = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='work_types')
    name = models.CharField(max_length=255)
    tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE, related_name='work_types')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='work_types')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип работы'
        verbose_name_plural = 'Типы работы'

class Order(models.Model):
    tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE, related_name='orders')
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE, related_name='orders')
    area = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tractor} - {self.area}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Seed(models.Model):
    place = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='seeds')
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
    name = models.CharField(max_length=255)
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


class Legal_Documents(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='legal_documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Правовые документы'
        verbose_name_plural = 'Правовые документы'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.CharField(max_length=255, choices=REVIEW_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Banner(models.Model):
    image = models.ImageField(upload_to='banner_images/')
    text = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
