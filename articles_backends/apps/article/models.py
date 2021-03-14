from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['code']
