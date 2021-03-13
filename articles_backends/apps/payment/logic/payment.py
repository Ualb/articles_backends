from apps.payment.models import Payment, PaymentDetail


def save_payment(data):
    payment = Payment()
    payment.save()
    for detail in data[payment_detail]:
        new_detail = PaymentDetail(
            code_article=detail['code_article'],
            id_payment=payment.id,
            quantity=detail['quantity']
        )
    return True
