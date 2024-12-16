import random
import string

from rest_framework import status
from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from shortener.models import ShortURL
from shortener.serializers import ShortURLReadSerializer, ShortURLCreateSerializer


class ShortURLsAPIView(ListCreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLReadSerializer

    def perform_create(self, serializer):
        # 중복 검사
        while True:
            code = ShortURL.generate_code()
            if not ShortURL.objects.filter(code=code).exists():
                break
        return serializer.save(code=code)

    def create(self, request, *args, **kwargs):
        serializer = ShortURLCreateSerializer(data=request.data)
        if serializer.is_valid():
            short_url = self.perform_create(serializer)
            return Response(data=ShortURLReadSerializer(short_url).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShortURLAPIView(APIView):
    def delete(self, request, code):
        short_url = get_object_or_404(ShortURL, code=code)
        short_url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
