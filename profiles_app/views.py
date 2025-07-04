from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPI(APIView):
    """ Testing the APIView with a dummy list """
    def get(self, request, format=None):
        shopping_list = ['salt', 'pepper', 'pepper spray', 'door knob']
        return Response({'message': 'Hello!', 'shopping_list':shopping_list})