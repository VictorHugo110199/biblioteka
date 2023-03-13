from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Copy, Borrow
from livros.models import Book
from django.forms.models import model_to_dict
from users.serializers import UserSerializer
from users.models import User

class CopySerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField(read_only=True)

    books_id = serializers.CharField(validators = [
        UniqueValidator(
            queryset=Copy.objects.all(),
            message='This book already has a copy.'
        )]
    )

    class Meta:
        model = Copy
        fields = ["id", "books_id", "amount", "copy_booked", "is_available", "book"]
        
    def get_book(self, obj) -> str:
        found_book = Book.objects.get(id=obj.books_id)
        returned_book = model_to_dict(found_book)
        returned_book.pop('following')
        return returned_book

class BorrowSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Borrow
        fields = ["id", "user", "copy", "borrowing_start_date", "return_date", "is_returned"]
        read_only_fields = ["id", "user", "copy", "borrowing_start_date", "return_date", "is_returned"]

    def update(self, instance, validated_data):
        copy = Copy.objects.filter(pk=instance.copy.id).first()

        copy.copy_booked -= 1

        copy.is_available = True

        copy.save()

        instance.is_returned=True

        instance.save()

        user = User.objects.filter(pk=validated_data["user"].id).first()

        user.is_allowed = True
        user.save()

        return instance