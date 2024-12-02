from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bot
from .serializers import BotSerializer

class BotAPI(APIView):
    def get(self, request):
        bot = Bot.objects.all()
        serializer = BotSerializer(bot, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BotSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                print(f"Error: {e}")
                return Response({'error': f'Error interno del servidor : {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
