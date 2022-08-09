from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.urls import reverse


class Watches(models.Model):
    SEX_CHOICES = (
        ('Мужские', 'Мужские'),
        ('Женские', 'Женские'),
        ('Унисекс', 'Унисекс')
    )
    name = models.CharField(max_length=50, verbose_name='Название', blank=True)
    brand = models.CharField(max_length=50, verbose_name='Бренд')
    series = models.CharField(max_length=50, verbose_name='Модель')
    price = models.IntegerField(verbose_name='Цена')
    sex = models.CharField(max_length=50, choices=SEX_CHOICES, default='UNISEX', verbose_name='Пол')
    image = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')
    mechanism = models.ForeignKey('WatchesMechanism', on_delete=models.PROTECT, blank=False, null=False, verbose_name='Механзм часов')
    company = models.ForeignKey('WatchesCompany', on_delete=models.PROTECT, blank=False, null=False, verbose_name='Компания изготовитель часов')

    def get_absolute_url(self):
        return reverse('watches_info', kwargs={'watches_id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар из магазина часов'
        verbose_name_plural = 'товары из магазина часов'
        ordering = ['-created_at']


class Phones(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название', blank=True)
    brand = models.CharField(max_length=50, verbose_name='Бренд')
    series = models.CharField(max_length=50, verbose_name='Модель')
    price = models.IntegerField(verbose_name='Цена')
    screen_diagonal = models.IntegerField(verbose_name='Диагональ экрана')
    image = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'товар из магазина смартфонов'
        verbose_name_plural = 'товары из магазина смартфонов'
        ordering = ['-created_at']


class WatchesMechanism(models.Model):
    mechanism = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('watches_mechanisms', kwargs={'mechanism_id': self.id})

    def __str__(self):
        return self.mechanism

    class Meta:
        verbose_name = 'Механизм часов'
        verbose_name_plural = 'Механизмы часов'
        ordering = ['mechanism']


class WatchesCompany(models.Model):
    company = models.CharField(max_length=50, blank=True)

    def get_absolute_url(self):
        return reverse('watches_companies', kwargs={'company_id': self.id})

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'Компания изготовитель часов'
        verbose_name_plural = 'Компании изготовители часов'
        ordering = ['company']


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
