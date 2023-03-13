from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Copy
from livros.models import Book
from django.forms.models import model_to_dict


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