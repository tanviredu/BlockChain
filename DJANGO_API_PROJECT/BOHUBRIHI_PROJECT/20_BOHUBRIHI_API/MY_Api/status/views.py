from .models import Status
from .serializers import StatusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


class StatusAPIView(APIView):
    def get(self, request, format=None):
        status_list = Status.objects.all()
        status_serializer = StatusSerializer(status_list, many=True)
        return Response(status_serializer.data)


class StatusListAPIView(ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
