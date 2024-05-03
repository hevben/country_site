from django.db import models

class Continent(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название континента')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Континент'
        verbose_name_plural = 'Континенты'

class Form(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название ФП')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Форма правления'
        verbose_name_plural = 'Формы правления'

class Country(models.Model):
    name = models.CharField(max_length = 100, verbose_name='Название страны')
    continents = models.ManyToManyField(Continent)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    c_code = models.CharField(max_length = 100, verbose_name='Код страны',default='none')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


# Create your models here.
