from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class HelloApiView(APIView):
    """Test APIView"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            "Uses HTTP methods as function (get, post, put, patch, delete)",
            "It's similar to a traditional Django View",
            "Gives you the most control over your logic",
            "It's mapped manually to URLs"
        ]

        return Response({"message": "Hello", "an_apivew": an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            message = "Hello {0}".format(name)
            return Response({"message": message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating the object."""

        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({"method": "delete"})
