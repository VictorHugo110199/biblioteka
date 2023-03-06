from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators = [
        UniqueValidator(
            queryset=User.objects.all(),
            message='This field must be unique.'
        )]
    )

    username = serializers.CharField(validators = [
        UniqueValidator(
            queryset=User.objects.all(),
            message='A user with that username already exists.'
        )]
    )

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name", "is_superuser"]
        extra_kwargs = {"password":{"write_only": True}}

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if validated_data['password']:
            instance.set_password(validated_data['password'])

        instance.save()

        return instance