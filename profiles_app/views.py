from rest_framework.views import APIView, status
from rest_framework.response import Response

from . import serializers


class HelloAPI(APIView):
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """ Testing the APIView with a dummy list """
        shopping_list = ['salt', 'pepper', 'pepper spray', 'door knob']
        return Response({'message': 'Hello!', 'shopping_list':shopping_list})
    

    def post(self, request):
        """ Creates a hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!!!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )
    

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})


    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})

