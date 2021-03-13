from django.db import models


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payment"
        ordering = ['id']


class PaymentDetail(models.Model):
    id = models.AutoField(primary_key=True)
    # you do not have permission to delete payments or items by this way (on_delete)
    code_article = models.ForeignKey(
        'article.Article', related_name='article', on_delete=models.DO_NOTHING)
    id_payment = models.ForeignKey(
        Payment, related_name='payment', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Payment Detail"
        verbose_name_plural = "Details"
        ordering = ['id']
