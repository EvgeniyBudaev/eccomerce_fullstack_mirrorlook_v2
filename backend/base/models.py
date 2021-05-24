from django.db import models
from django.contrib.auth.models import User


class Catalog(models.Model):
  name = models.CharField(max_length=255, verbose_name='Название каталога')
  image = models.ImageField(null=True, blank=True, verbose_name='Изображение каталога')
  catalogSlug = models.SlugField(max_length=255, unique=True, verbose_name='URL каталога')
  createdAt = models.DateTimeField(auto_now_add=True)
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.name


class Category(models.Model):
  catalogId = models.ForeignKey(Catalog, null=True, verbose_name='Каталог',
                                  on_delete=models.CASCADE)
  name = models.CharField(max_length=255, verbose_name='Имя категории')
  image = models.ImageField(null=True, blank=True, verbose_name='Изображение категории')
  categorySlug = models.SlugField(max_length=255, unique=True, verbose_name='URL категории')
  createdAt = models.DateTimeField(auto_now_add=True)
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.name


class Product(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # При True Django сохранит пустое значение как NULL в базе данных. Значение по умолчанию – False.
  categoryId = models.ForeignKey(Category, null=True, verbose_name='Категория', on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Наименование')
  productSlug = models.SlugField(max_length=255, unique=True, verbose_name='URL продукта')
  image = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/', default='/placeholder.png', verbose_name='Изображение продукта')
  productPhoto1 = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/')
  productPhoto2 = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/')
  productPhoto3 = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/')
  productPhoto4 = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/')
  description = models.TextField(null=True, blank=True, verbose_name='Описание')
  rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Рейтинг')
  numReviews = models.IntegerField(null=True, blank=True, verbose_name='Комментарии')
  price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Цена')
  countInStock = models.IntegerField(null=True, blank=True, default=0, verbose_name='Кол-во товара')
  code = models.CharField(max_length=32, null=True, blank=True, verbose_name='Артикул')
  colorFrame = models.CharField(max_length=64, null=True, blank=True, verbose_name='Цвет рамы')
  colorMirror = models.CharField(max_length=64, null=True, blank=True, verbose_name='Цвет зеркала')
  baseMirror = models.CharField(max_length=64, null=True, blank=True, verbose_name='Цвет основы')
  height = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Высота')
  width = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Ширина')
  weight = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Вес')
  typeOfInstallation = models.CharField(max_length=64, null=True, blank=True, verbose_name='Тип установки')
  typeOfMounting= models.CharField(max_length=64, null=True, blank=True, verbose_name='Тип навески')
  heightWithoutFrame = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Высота без рамы")
  weightWithoutFrame = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Ширина без рамы")
  faced = models.BooleanField(default=True, null=True, blank=True, verbose_name='Фацет')
  form = models.CharField(max_length=64, null=True, blank=True, verbose_name='Форма')
  appointment = models.CharField(max_length=200, null=True, blank=True, verbose_name='Назначение')
  materialMirror = models.CharField(max_length=200, null=True, blank=True, verbose_name='Материал зеркала')
  materialFrame = models.CharField(max_length=200, null=True, blank=True, verbose_name='Материал рамы')
  countryBrand = models.CharField(max_length=64, null=True, blank=True, verbose_name='Страна бренда')
  countryManufacturer = models.CharField(max_length=64, null=True, blank=True, verbose_name='Страна производства')
  manufacturer = models.CharField(max_length=64, null=True, blank=True, verbose_name='Производитель')
  createdAt = models.DateTimeField(auto_now_add=True)
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Продукт'
    verbose_name_plural = 'Продукты'
    ordering = ['-createdAt']  # сортировка в админке


class Review(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Наименование')
  rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Рейтинг')
  comment = models.TextField(null=True, blank=True, verbose_name='Комментарий')
  createdAt = models.DateTimeField(auto_now_add=True)
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self.rating)


class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  paymentMethod = models.CharField(max_length=200, null=True, blank=True, verbose_name='Способ оплаты')
  taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Налог')
  shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Цена доставки')
  totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Итоговая сумма')
  isPaid = models.BooleanField(default=False, verbose_name='Статус оплаты')
  paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True, verbose_name='Дата оплаты')
  isDelivered = models.BooleanField(default=False, verbose_name='Статус доставки')
  deliveredAt = models.DateTimeField(auto_now_add=True, verbose_name='Дата доставки')
  createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Дата создания')
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self.createdAt)


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
  postalCode = models.CharField(max_length=200, null=True, blank=True, verbose_name='Индекс')
  country = models.CharField(max_length=200, null=True, blank=True, verbose_name='Страна')
  shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Стоимость доставки')
  id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self.address)
