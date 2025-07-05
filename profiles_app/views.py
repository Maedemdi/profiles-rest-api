from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication

from . import serializers, models, permissions


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
            message = f'Hello {name}! This is produced by an APIView.'
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
    

class HelloViewset(viewsets.ViewSet):
    """ Learning how to use Viewsets """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Testing the list action with a random list """
        movies = ['Fight Club', 'Eraserhead', 'The Clockwork Orange']
        return Response({'message':'Hi','movies': movies})
    

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hi {name}! This is produced by a Viewset.'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})


    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})


    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
