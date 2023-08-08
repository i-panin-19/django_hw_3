# Generated by Django 4.2.4 on 2023-08-06 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='shop/', verbose_name='Изображение')),
                ('category', models.CharField(max_length=150, verbose_name='Категория')),
                ('purchase_price', models.IntegerField(verbose_name='Цена покупки')),
                ('date_creation', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('date_change', models.DateField(blank=True, null=True, verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
    ]
