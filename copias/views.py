from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.permissions import IsCollaborator
from .serializers import CopySerializer
from .models import Copy

class CopyView (CreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]

class CopyDetailView (RetrieveUpdateDestroyAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]


class CopyListView (ListCreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]


# Create your views here.
