from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        read_only_fields = ["users"]
    
    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)
    
    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data:
            setattr(instance, key, value)
        instance.save()

        return instance
    
