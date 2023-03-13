from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, UpdateAPIView, ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from livros.permissions import isAdminOrGetOnly
from django.shortcuts import get_object_or_404
from livros.models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import CopySerializer, BorrowSerializer
from .models import Copy, Borrow
import datetime
from rest_framework.views import status
from rest_framework.response import Response
from users.models import User
from .permissions import IsAdminUser


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

class BorrowView(CreateAPIView):
    serializer_class = BorrowSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Borrow.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except ReferenceError:
            return Response({"message": "Unavailable copies of this book"}, status.HTTP_400_BAD_REQUEST)
        except PermissionError:
            return Response({"message": "You have not returned your books"}, status.HTTP_401_UNAUTHORIZED)
            
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        copy = get_object_or_404(Copy, pk=self.kwargs["pk"])

        if copy.is_available == False:
            raise ReferenceError("Unavailable copies of this book")
        
        if Borrow.objects.filter(user=self.request.user, return_date__lt=datetime.datetime.now(), is_returned=False).count() > 0 or self.request.user.is_allowed == False:
            self.request.user.is_allowed=False
            self.request.user.save()
            raise PermissionError("You have not returned your books")
        
        copy.copy_booked += 1 

        if copy.copy_booked == copy.amount:
            copy.is_available = False

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

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class BorrowListView(ListAPIView):
    serializer_class = BorrowSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Borrow.objects.filter(user=self.request.user)
    
class BorrowListCollaboratorView(ListAPIView):
    serializer_class = BorrowSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs["pk"])
        return Borrow.objects.filter(user=user)
    
    

# Create your views here.
