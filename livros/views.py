from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer
from .models import Book
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import isAdminOrGetOnly
from django.shortcuts import get_object_or_404
from users.models import User
from .tasks import send_notification



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


class FollowingView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request: Request, book_id: int) -> Response:
        user_requester = request.user.id

        book = get_object_or_404(Book, id=book_id)
        user = get_object_or_404(User, id=user_requester)

        book.following.add(user)
        send_notification(user, book)

        return Response({"message": f"Você está seguindo o livro {book.title}!"}, status.HTTP_201_CREATED)

