from django.contrib.admin import ModelAdmin, register
from .models import Article


@register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ('code', 'description', 'price', 'cost', 'is_active')
    list_filter = ('code', 'is_active')
    ordering = ('code', 'price', 'cost')
