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
    id_article = models.ForeignKey(
        'article.Article', related_name='article', on_delete=models.DO_NOTHING)
    id_payment = models.ForeignKey(
        Payment, related_name='payment', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    # ok, imagine the case, make a purchase and then you modify the cost of the list of items,
    # then, the cost of the payment is modified, the solution is to save the subtotal
    sub_total = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Payment Detail"
        verbose_name_plural = "Details"
        ordering = ['id']
