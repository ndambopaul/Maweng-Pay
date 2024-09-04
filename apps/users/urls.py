from django.urls import path

from apps.users.views import RegisterUserAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh-token/", TokenRefreshView.as_view(), name="refresh-token"),
    path("verify-token/", TokenVerifyView.as_view(), name="verify-token"),
]
