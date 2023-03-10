from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CopySerializer
from .models import Copy
from livros.permissions import isAdminOrGetOnly
from django.shortcuts import get_object_or_404
from livros.models import Book


class CopyView(ListCreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.request.data['books_id'])
        serializer.save(books = book)

    permission_classes = [isAdminOrGetOnly]
    authentication_classes = [JWTAuthentication]

class CopyDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer
    
    permission_classes = [isAdminOrGetOnly]
    authentication_classes = [JWTAuthentication]


# Create your views here.
