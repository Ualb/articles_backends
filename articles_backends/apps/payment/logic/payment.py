from apps.payment.models import Payment, PaymentDetail
from apps.payment.constraints import articles_validator
from apps.article.models import Article


def save_payment(data):
    payment = Payment()
    payment.save()
    for detail in data['payment_detail']:
        if articles_validator(detail['id_article']):
            article = Article.objects.get(id=detail['id_article'])
            PaymentDetail(
                id_article=article,
                id_payment=payment,
                quantity=detail['quantity'],
                sub_total=article.price * detail['quantity']
            ).save()
        else:
            continue
    return payment
