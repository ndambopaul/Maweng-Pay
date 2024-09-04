import requests
from rest_framework import status

from django.conf import settings
from apps.users.models import User
from apps.intasend.models import IntasendMpesaData
from apps.intasend.stk_push_reponse_creator import entangle_stk_push_response


class IntasendTransactionProcessor:
    def __init__(self):
        self.headersList = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {settings.INTASEND_SECRET_KEY}",
        }

    def trigger_stk_push(self, phone_number: str, amount: str, user: User):
        try:
            response = requests.post(
                f"{settings.INTASEND_BASE_URL}/payment/mpesa-stk-push/",
                json={"phone_number": phone_number, "amount": amount},
                headers=self.headersList,
            )
            if response.ok:
                data = entangle_stk_push_response(response.json())
                record = IntasendMpesaData.objects.create(user=user, **data)

                return {
                    "message": "Payment successfully initiated",
                    "invoice_id": record.invoice_id,
                    "status": status.HTTP_201_CREATED,
                }
            else:
                return {
                    "message": "Payment initiation failed, Try again!",
                    "status": status.HTTP_400_BAD_REQUEST,
                }
        except Exception as e:
            raise e

    def verify_payment_status(self, invoice_id: str):
        try:
            payment_record = IntasendMpesaData.objects.filter(
                invoice_id=invoice_id
            ).first()
            response = requests.post(
                f"{settings.INTASEND_BASE_URL}/payment/status/",
                json={"invoice_id": invoice_id},
                headers=self.headersList,
            )

            if response.ok:
                response_data = response.json()

                payment_state = response_data["invoice"]["state"]
                charges = response_data["invoice"]["charges"]
                net_amount = response_data["invoice"]["net_amount"]

                if payment_record:
                    payment_record.state = payment_state
                    payment_record.charges = charges
                    payment_record.net_amount = net_amount
                    payment_record.verified = (
                        True if payment_state == "COMPLETE" else False
                    )
                    payment_record.save()

                    if payment_state == "COMPLETE":
                        return {
                            "message": "Payment successfully verified!",
                            "status": status.HTTP_201_CREATED,
                        }
                    elif payment_state == "PROCESSING":
                        return {
                            "message": "Payment is still being processed, check again after 1 minute",
                            "status": status.HTTP_200_OK,
                        }
                    else:
                        return {
                            "message": "Payment failed, please contact support team and share your invoice id",
                            "status": status.HTTP_400_BAD_REQUEST,
                        }
            else:
                return {
                    "message": "Request failed, try again in 2 minutes",
                    "status": status.HTTP_400_BAD_REQUEST,
                }
        except Exception as e:
            raise e
