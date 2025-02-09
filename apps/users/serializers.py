from rest_framework import serializers
from apps.users.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "gender",
            "phone_number",
            "role",
        ]
