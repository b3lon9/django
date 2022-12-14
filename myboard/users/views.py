from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics

from users.serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from users.models import Profile

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data   # 토큰을 받아옴
        return Response({"token":token.key}, status=status.HTTP_200_OK)

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer