from rest_framework.views import APIView, Response, Request, status
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
        send_notification(user, book, "following")

        return Response({"message": f"Você está seguindo o livro {book.title}!"}, status.HTTP_201_CREATED)


class GetFollowingView(APIView):
    authentication_classes= [JWTAuthentication]

    def get(self, request:Request) -> Response:
        user = get_object_or_404(User, id=request.user.id)

        book_followed = Book.objects.filter(
            following=user
        )

        serializer = BookSerializer(book_followed, many=True)

        return Response({"user_id": user.id, "books_followed": serializer.data}, status.HTTP_200_OK)
    

class UnfollowView(APIView):
    authentication_classes= [JWTAuthentication]

    def delete(self, request: Request, book_id:int) -> Response:

        book = get_object_or_404(Book, id=book_id)
        user = get_object_or_404(User, id=request.user.id)

        book.following.remove(user)
        send_notification(user, book, "unfollowing")

        return Response(status=status.HTTP_204_NO_CONTENT)