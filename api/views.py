from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import permissions, exceptions

from api.authentication import CustomJwtAuthentication, IsAuthenticated
from api.utils import (
    settings,
    generate_access_token,
    console_log,
)


class Index(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response(status=status.HTTP_200_OK, data={})


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username", None)
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        user = authenticate(request, email=email, username=username, password=password)

        if not user:
            raise exceptions.AuthenticationFailed("Invalid credentials.")

        if not user.is_active:
            raise exceptions.AuthenticationFailed("User account is disabled.")

        payload = {"token": generate_access_token(user)}
        return Response(payload, status=status.HTTP_200_OK)


class RequestView(APIView):
    authentication_classes = [CustomJwtAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request)
        return Response(status=status.HTTP_200_OK)
