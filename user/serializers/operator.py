from django.contrib.auth.hashers import make_password
from rest_framework import serializers, request, status

from user.models import User


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'password', 'phone_number')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ('id', 'role',)

    def create(self, validated_data):
        user = self.context['request'].user
        username = validated_data['username']
        if not user.is_authenticated:
            raise serializers.ValidationError(status.HTTP_409_CONFLICT,
                                              'You are not authenticated')
        if user.role != User.Role.ADMIN:
            raise serializers.ValidationError(
                status.HTTP_409_CONFLICT,
                "Only admin can create users"
            )
        validated_data['user'] = User.objects.get(id=user.id)
        validated_data['role'] = User.Role.USER
        validated_data['password'] = make_password(
            validated_data['password']
        )
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                status.HTTP_409_CONFLICT,
                'Username already exists'
            )

        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance

