from django.db import models
from apps.core.models import AbstractBaseModel


# Create your models here.
class IntasendMpesaData(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    transaction_id = models.CharField(max_length=500)
    invoice_id = models.CharField(max_length=255)
    provider = models.CharField(max_length=255, null=True)
    charges = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    api_ref = models.CharField(max_length=255, null=True)
    currency = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255)
    mpesa_reference = models.CharField(max_length=255, null=True)
    amount_transacted = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    net_amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    phone_number = models.CharField(max_length=255)
    customer = models.JSONField(default=dict)
    transaction_timestamp = models.DateTimeField(null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class IntasendPaymentLink(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    payment_link_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    is_active = models.BooleanField()
    amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    usage_limit = models.IntegerField()
    qrcode = models.URLField()
    url = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    mobile_tarrif = models.CharField(max_length=255)
    card_tarrif = models.CharField(max_length=255)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.title