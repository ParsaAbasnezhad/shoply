from django.db import models


class Category(models.Model):
    """دسته‌بندی محصولات (مثلاً: اسپرسو، عربیکا، دستگاه آسیاب، قطعات و ...)"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    PRODUCT_TYPES = [
        ('coffee', 'Coffee'),       # قهوه
        ('machine', 'Coffee Machine'),  # دستگاه
        ('part', 'Coffee Part'),    # قطعه
    ]

    name = models.CharField(max_length=200, verbose_name="نام محصول")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت")
    stock = models.PositiveIntegerField(default=0, verbose_name="موجودی")
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="تصویر")
    type = models.CharField(max_length=20, choices=PRODUCT_TYPES, default='coffee', verbose_name="نوع محصول")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="دسته‌بندی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین تغییر")

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"