from rest_framework import serializers
from apps.intasend.models import IntasendMpesaData, IntasendPaymentLink


class IntesendLipaNaMpesaSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=255)
    amount = serializers.DecimalField(max_digits=100, decimal_places=2)


class IntasendPaymentStatusCheckSerializer(serializers.Serializer):
    invoice_id = serializers.CharField(max_length=255)
    checkout_id = serializers.CharField(max_length=255, required=False)
    signature = serializers.CharField(max_length=255, required=False)


class IntasendMpesaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntasendMpesaData
        fields = "__all__"

class IntasendPaymentLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntasendPaymentLink
        fields = "__all__"

class CreateIntasendPaymentLinkSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    amount = serializers.DecimalField(max_digits=100, decimal_places=2)