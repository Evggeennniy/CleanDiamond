from django.db import models


class Category(models.Model):
    """Модель категорії послуг"""
    name = models.CharField(max_length=255, unique=True, verbose_name="Назва категорії")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Service(models.Model):
    """Модель послуги, яка прив'язана до категорії"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="services", verbose_name="Категорія")
    name = models.CharField(max_length=255, unique=True, verbose_name="Назва послуги")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"
