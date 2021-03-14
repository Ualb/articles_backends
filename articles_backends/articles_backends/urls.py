from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.article.views import ArticleView
from apps.payment.views import PaymentView

router = routers.DefaultRouter()
# our endpoints
router.register(r'articles', ArticleView)
router.register(r'payments', PaymentView)

schema_view = get_schema_view(
    openapi.Info(
        title="Articles BackEnd Rest API",
        default_version='v1',
        description="Main data service for Article App\n\n"
        "This service is make with Django [Rest Framework](https://www.django-rest-framework.org) and SQLite database using [Django](https://www.djangoproject.com) Model ORM.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ulises050794@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
