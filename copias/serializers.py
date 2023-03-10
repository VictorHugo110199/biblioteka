from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Copy

class CopySerializer(serializers.ModelSerializer):

    # books_id = serializers.CharField(validators = [
    #     UniqueValidator(
    #         queryset=Copy.objects.all(),
    #         message='This book already has a copy.'
    #     )]
    # )
    class Meta:
        model = Copy
        fields = ["id", "amount", "books_id", "copy_booked", "is_available"]