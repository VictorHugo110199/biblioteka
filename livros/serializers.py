from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    title = serializers.CharField(validators = [
        UniqueValidator(
            queryset=Book.objects.all(),
            message='This field must be unique.'
        )]
    )
    class Meta:
        model = Book
        fields = ["id", "title", "author", "number_pages", "gender", "following"]
        extra_kwargs = {"following":{"read_only": True}}

class BookFollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["id", "title", "author", "number_pages", "gender"]

    
