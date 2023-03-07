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
        fields = ["id", "title", "author", "number_pages", "gender"]
    
    # def create(self, validated_data: dict) -> Book:
    #     return Book.objects.create(**validated_data)
    
    # def update(self, instance: Book, validated_data: dict) -> Book:
    #     for key, value in validated_data:
    #         setattr(instance, key, value)
    #     instance.save()

    #     return instance
    
