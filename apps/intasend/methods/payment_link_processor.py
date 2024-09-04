import requests
from rest_framework import status


from django.conf import settings
from apps.users.models import User
from apps.intasend.models import IntasendPaymentLink

class IntasendPaymentLinkProcessor:
    def __init__(self):
        self.headersList = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {settings.INTASEND_SECRET_KEY}",
        }

    def create_payment(self, payload: dict, user: User):
        try:
            response = requests.post(f"{settings.INTASEND_BASE_URL}/paymentlinks/", json=payload, headers=self.headersList)

            if response.ok:
                data = response.json()
                record = IntasendPaymentLink.objects.create(
                    user=user,
                    title=data["title"],
                    is_active=data["is_active"],
                    redirect_url=data["redirect_url"],
                    amount=data["amount"],
                    usage_limit=data["usage_limit"],
                    qrcode=data["qrcode_file"],
                    url=f"f{settings.INTASEND_URL}{data["url"]}",
                    mobile_tarrif=data["mobile_tarrif"],
                    card_tarrif=data["card_tarrif"],
                    redirect_url=settings.INSTASEND_PAYMENT_REDIRECT_URL
                )
                return { "message": "Payment Link Created Successfully", "payment_link": record.url, "status": status.HTTP_201_CREATED }
            else:
                return { "message": "Payment link creation failed, try again", "status": status.HTTP_400_BAD_REQUEST }

        except Exception as e:
            raise { "message": str(e), "status": status.HTTP_400_BAD_REQUEST }

        

