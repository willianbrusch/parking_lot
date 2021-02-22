from django.urls import path
from .views import PriceView

urlpatterns = [
    path('pricings/', PriceView.as_view())
]
