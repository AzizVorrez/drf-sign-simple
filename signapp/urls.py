from django.urls import path
from signapp.views import *

urlpatterns = [
    path('create', CreateUserView.as_view(), name = "create-user"),
]