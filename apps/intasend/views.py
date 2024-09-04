from django.shortcuts import render
import requests

from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from apps.intasend.models import IntasendMpesaData
from apps.intasend.serializers import (
    IntesendLipaNaMpesaSerializer,
    IntasendMpesaDataSerializer,
    IntasendPaymentStatusCheckSerializer,
)

from apps.intasend.methods.transactions_processor import IntasendTransactionProcessor
# Create your views here.


class IntasendLipaNaMpesaAPIView(generics.CreateAPIView):
    serializer_class = IntesendLipaNaMpesaSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            phone_number = serializer.validated_data.get("phone_number")
            amount = serializer.validated_data.get("amount")

            try:
                processor = IntasendTransactionProcessor()
                res = processor.trigger_stk_push(phone_number=phone_number, amount=amount, user=user)
                return Response(res)
            except Exception as e:
                raise Response({ "message": str(e) }, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IntasendMpesaDataAPIView(generics.ListAPIView):
    queryset = IntasendMpesaData.objects.all().order_by("-created")
    serializer_class = IntasendMpesaDataSerializer


class IntasendPaymentStatusCheckAPIView(generics.CreateAPIView):
    serializer_class = IntasendPaymentStatusCheckSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            invoice_id = serializer.validated_data.get("invoice_id")
            try:
                processor = IntasendTransactionProcessor()
                res = processor.verify_payment_status(invoice_id=invoice_id)
                return Response(res)
            except Exception as e:
                return Response({ "message": str(e) }, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IntasendCheckoutRedirectAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print(self.request.query_params)
        print(request.query_params)
        print(args)
        print(kwargs)
        return Response({ "message": "Am just testing this out" }, status=status.HTTP_200_OK)
    

