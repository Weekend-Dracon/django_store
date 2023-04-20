from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name="Название категории", max_length=150, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    title = models.CharField(verbose_name="Название подкатегории", max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Product(models.Model):
    PRODUCT_TYPES = (
        ("new", "New"),
        ("sale", "Sale"),
        ("sold", "Sold"),
    )
    title = models.CharField(verbose_name="Название продукта", max_length=150, unique=True)
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена", default=0)
    quantity = models.IntegerField(verbose_name="Количество продукта", default=0)
    views = models.IntegerField(verbose_name="Количество просмотров", default=0)
    product_type = models.CharField(
        max_length=10,
        choices=PRODUCT_TYPES,
        blank=True,
        null=True,
        default=""
    )
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, verbose_name="Подкатегория", null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория", null=True)


class ProductImage(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to="products/", null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
# CategoryModel
#     title
# SubCategoryModel
#     title
#     category_id
# Product
    # title
    # description
    # price
    # quantity
    # product_type (new, sale, sold)
    # category
    # views
# ProductImage
    # photo
    # product_id
