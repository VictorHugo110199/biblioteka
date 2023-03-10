from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from livros.permissions import isAdminOrGetOnly
from django.shortcuts import get_object_or_404
from livros.models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import CopySerializer, BorrowSerializer
from .models import Copy, Borrow
import datetime
from rest_framework.views import status

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

class BorrowView(ListCreateAPIView):
    serializer_class = BorrowSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Borrow.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        copy = get_object_or_404(Copy, pk=self.kwargs["pk"])

        if copy.amount < 1:
            return self.response({"message": "Unavailable copies of this book"}, status.HTTP_400_BAD_REQUEST)
        
        if Borrow.objects.filter(user=self.request.user, return_date__lt=datetime.datetime.now(), is_returned=False).count() > 0 or self.request.user.is_allowed == False:
            self.request.user.is_allowed=False
            self.request.user.save()
            return self.response({"message": "You have not returned your books"}, status.HTTP_401_UNAUTHORIZED)
        
        copy.amount -= 1
        copy.save()

        return_date = datetime.datetime.now() + datetime.timedelta(days=7)

        if return_date.strftime("%a") == "Sat":
            return_date = return_date + datetime.timedelta(days=2)
        if return_date.strftime("%a") == "Sun":
            return_date = return_date + datetime.timedelta(days=1)

        serializer.save(user=self.request.user, copy=copy, return_date=return_date)
    
class BorrowDetailView(UpdateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    

# Create your views here.
