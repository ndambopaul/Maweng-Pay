from django.urls import path
from apps.intasend.views import (
    IntasendLipaNaMpesaAPIView,
    IntasendMpesaDataAPIView,
    IntasendPaymentStatusCheckAPIView,
    IntasendCheckoutRedirectAPIView,
)

urlpatterns = [
    path("lipa-na-mpesa/", IntasendLipaNaMpesaAPIView.as_view(), name="intasend-lipa-na-mpesa"),
    path("mpesa-data/", IntasendMpesaDataAPIView.as_view(), name="intasend-mpesa-data"),
    path("status-check/", IntasendPaymentStatusCheckAPIView.as_view(), name="intasend-payment-status-check"),
    path("checkout-callback/", IntasendCheckoutRedirectAPIView.as_view(), name="intasend-checkout-callback"),
]
