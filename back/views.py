from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bots
from .serializers import BotsSerializer

class BotsAPI(APIView):
    def get(self, request):
        bots = Bots.objects.all()
        serializer = BotsSerializer(bots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BotsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
