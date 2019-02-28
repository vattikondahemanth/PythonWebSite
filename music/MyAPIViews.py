from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Song
from .serializers import StockSerializer


class SongsView(APIView):
    def get(self, *args, **kwargs):
        songs = Song.objects.all()
        serializer = StockSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self):
        pass


#===========================