from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message="A user with this email already exists.")]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'phone', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name')
        )
        return user



# from django.contrib.auth.models import User
# from rest_framework import serializers, validators
#
#
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'email', 'first_name', 'last_name')
#
#         extra_kwargs = {
#             "password": {"write_only": True},
#             "email": {
#                 "required": True,
#                 "allow_blank": False,
#                 "validator": [
#                     validators.UniqueValidator(
#                         User.objects.all(), "A User with the Email already exists"
#                     )
#                 ]
#             }
#         }
#
#
#     def create(self, validated_data):
#         username = validated_data.get('username')
#         password = validated_data.get('password')
#         email = validated_data.get('email')
#         first_name = validated_data.get('first_name')
#         last_name = validated_data.get('last_name')
#
#         user = User.objects.create(
#             username=username,
#             password=password,
#             email=email,
#             first_name=first_name,
#             last_name=last_name
#         )
#
#         return user