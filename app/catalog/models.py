from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Назва категорії")
    icon = models.ImageField(verbose_name='Зображення', upload_to='images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="services", verbose_name="Категорія")
    name = models.CharField(max_length=255, unique=True, verbose_name="Назва послуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"
