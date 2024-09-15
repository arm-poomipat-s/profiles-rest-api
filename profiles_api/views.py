from rest_framework.views import APIView
from rest_framework.response import Response 



class HelloApiView(APIView):
    """Test API view"""
    
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP mdthods as fucntion (get, post , patch, put, delted)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manally to URLs',
        ]
        
        return Response({'message':'Hello','an_apiview': an_apiview})