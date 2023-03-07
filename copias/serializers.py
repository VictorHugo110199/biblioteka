from rest_framework import serializers
from .models import Copy

class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["amount", "books"]