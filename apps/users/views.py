from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, status

from apps.users.models import User
from apps.users.serializers import RegisterUserSerializer


# Create your views here.
class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(
                {"success": "User successfully registered"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
