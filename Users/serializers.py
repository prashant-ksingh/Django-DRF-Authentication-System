from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Ensures password is write-only
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class VerificationSerializer(serializers.Serializer):
    email_or_username = serializers.CharField(max_length=100)
    otp = serializers.CharField(max_length=6)

class LoginSerializer(serializers.Serializer):
    email_or_username = serializers.CharField(max_length=100)
    otp = serializers.CharField()

class ForgotPasswordSerializer(serializers.Serializer):
    email_or_username = serializers.CharField(max_length=100)

class ResetPasswordSerializer(serializers.Serializer):
    email_or_username = serializers.CharField(max_length=100)
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(min_length=8)  # Example: Enforce minimum password length
