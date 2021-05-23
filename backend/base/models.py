from django.db import models
from django.contrib.auth.models import User


class Catalog(models.Model):
  name = models.CharField(max_length=255, verbose_name='Название каталога')
  image = models.ImageField(null=True, blank=True, verbose_name='Изображение каталога')
  catalog_slug = models.SlugField(max_length=255, unique=True, verbose_name='URL каталога')
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.name


class Category(models.Model):
  catalog_id = models.ForeignKey(Catalog, null=True, verbose_name='Каталог',
                                  on_delete=models.CASCADE)
  name = models.CharField(max_length=255, verbose_name='Имя категории')
  image = models.ImageField(null=True, blank=True, verbose_name='Изображение категории')
  category_slug = models.SlugField(max_length=255, unique=True, verbose_name='URL категории')
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.name


class Product(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # При True Django сохранит пустое значение как NULL в базе данных. Значение по умолчанию – False.
  category_id = models.ForeignKey(Category, null=True, verbose_name='Категория', on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Наименование')
  product_slug = models.SlugField(max_length=255, unique=True, verbose_name='URL продукта')
  image = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/', default='/placeholder.png', verbose_name='Изображение продукта')
  product_photo1 = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/')
  product_photo2 = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/')
  product_photo3 = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/')
  product_photo4 = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/')
  description = models.TextField(null=True, blank=True, verbose_name='Описание')
  rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Рейтинг')
  num_reviews = models.IntegerField(null=True, blank=True, verbose_name='Комментарии')
  price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Цена')
  count_in_stock = models.IntegerField(null=True, blank=True, default=0, verbose_name='Кол-во товара')
  code = models.CharField(max_length=32, null=True, blank=True, verbose_name='Артикул')
  color_frame = models.CharField(max_length=64, null=True, blank=True, verbose_name='Цвет рамы')
  color_mirror = models.CharField(max_length=64, null=True, blank=True, verbose_name='Цвет зеркала')
  base_mirror = models.CharField(max_length=64, null=True, blank=True, verbose_name='Цвет основы')
  height = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Высота')
  width = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Ширина')
  weight = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Вес')
  type_of_installation = models.CharField(max_length=64, null=True, blank=True, verbose_name='Тип установки')
  type_of_mounting= models.CharField(max_length=64, null=True, blank=True, verbose_name='Тип навески')
  heightWithoutFrame = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Высота без рамы")
  weightWithoutFrame = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Ширина без рамы")
  faced = models.BooleanField(default=True, null=True, blank=True, verbose_name='Фацет')
  form = models.CharField(max_length=64, null=True, blank=True, verbose_name='Форма')
  appointment = models.CharField(max_length=200, null=True, blank=True, verbose_name='Назначение')
  material_mirror = models.CharField(max_length=200, null=True, blank=True, verbose_name='Материал зеркала')
  material_frame = models.CharField(max_length=200, null=True, blank=True, verbose_name='Материал рамы')
  country_brand = models.CharField(max_length=64, null=True, blank=True, verbose_name='Страна бренда')
  country_manufacturer = models.CharField(max_length=64, null=True, blank=True, verbose_name='Страна производства')
  manufacturer = models.CharField(max_length=64, null=True, blank=True, verbose_name='Производитель')
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Продукт'
    verbose_name_plural = 'Продукты'
    ordering = ['-created_at']  # сортировка в админке


class Review(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Наименование')
  rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Рейтинг')
  comment = models.TextField(null=True, blank=True, verbose_name='Комментарий')
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self.rating)


class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  payment_method = models.CharField(max_length=200, null=True, blank=True, verbose_name='Способ оплаты')
  tax_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Налог')
  shipping_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Цена доставки')
  total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Итоговая сумма')
  is_paid = models.BooleanField(default=False, verbose_name='Статус оплаты')
  paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True, verbose_name='Дата оплаты')
  is_delivered = models.BooleanField(default=False, verbose_name='Статус доставки')
  delivered_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата доставки')
  created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Дата создания')
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self.created_at)


class OrderItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Наименование')
  quantity = models.IntegerField(null=True, blank=True, default=0, verbose_name='Кол-во')
  price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Цена')
  image = models.CharField(max_length=200, null=True, blank=True, verbose_name='Фото')
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self.name)


class ShippingAddress(models.Model):
  order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
  address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Адрес')
  city = models.CharField(max_length=200, null=True, blank=True, verbose_name='Город')
  postal_code = models.CharField(max_length=200, null=True, blank=True, verbose_name='Индекс')
  country = models.CharField(max_length=200, null=True, blank=True, verbose_name='Страна')
  shipping_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Стоимость доставки')
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self.address)
