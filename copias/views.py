from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CopySerializer
from .models import Copy

class CopyView (CreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

class CopyDetailView (RetrieveUpdateDestroyAPIView, ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

# Create your views here.
