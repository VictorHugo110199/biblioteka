from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer
from .models import Book
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import isAdminOrGetOnly

class BookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [isAdminOrGetOnly]
    authentication_classes = [JWTAuthentication]

class BookDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [isAdminOrGetOnly]
    authentication_classes = [JWTAuthentication]


