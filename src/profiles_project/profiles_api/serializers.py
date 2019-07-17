from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        # model to be used by this serializer
        model = models.UserProfile
        # the fields this serializer will manage
        fields = ("id", "email", "name", "password")
        # make password field write-only, security-wise: password must not be read
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Overrides model manager's create method. Creates and returns a new user."""

        # create new user object using the validated data
        user = models.UserProfile(
            email=validated_data.get("email"),
            name=validated_data.get("name")
        )
        # use the spaciale set_password to encrypt the password
        user.set_password(validated_data.get("password"))
        user.save()

        return user
