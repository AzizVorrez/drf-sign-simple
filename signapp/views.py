from django.contrib.auth.models import User
from rest_framework import generics
from signapp.serializers import *

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
