from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.article.views import ArticleView
from apps.payment.views import PaymentView

router = routers.DefaultRouter()
# our endpoints
router.register(r'articles', ArticleView)
router.register(r'payments', PaymentView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
