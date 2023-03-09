from rest_framework import serializers
from .models import Copy, Borrow

class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["amount", "books"]

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ["id", "user", "copy", "borrowing_start_date", "return_date", "is_returned"]
        read_only_fields = ["id", "user", "copy", "borrowing_start_date", "return_date", "is_returned"]
    
    def update(self, instance, validated_data):
        copy = Copy.objects.filter(pk=instance.copy.id).first()
        copy.amount += 1
        copy.save()

        instance.is_returned=True
        instance.save()
        
        return instance
