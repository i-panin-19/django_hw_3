from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='shop/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена покупки')
    date_creation = models.DateField(**NULLABLE, verbose_name='Дата создания')
    date_change = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class BlogEntry(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, **NULLABLE, verbose_name='slug')
    content = models.TextField(verbose_name='Содержимое')
    photo = models.ImageField(upload_to='shop/', **NULLABLE, verbose_name='Изображение')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    views = models.IntegerField(default=0, verbose_name='Просмотров')
    date_creation = models.DateField(**NULLABLE, verbose_name='Дата создания')
    publication = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f'{self.title} ({self.product} {self.publication})'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'записи блога'
