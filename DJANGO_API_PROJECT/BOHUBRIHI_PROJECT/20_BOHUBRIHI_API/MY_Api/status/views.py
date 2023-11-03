from .models import Status
from .serializers import StatusSerializer, StatusUpdateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, parsers, viewsets
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


## JUST ONE VIEW TO DO EVERY THING
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


## FULL COMPACT


## LIST AND POST
class GenericListPostView(ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    ## we need parser to work with
    ## fila handling
    ## we need both parser
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class GenericRetUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"
    ## Update need parser too
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


##


## THIS IS VERY RAW
class StatusAPIView(APIView):
    def get(self, request, format=None):
        status_list = Status.objects.all()
        status_serializer = StatusSerializer(status_list, many=True)
        return Response(status_serializer.data)


class StatusListAPIView(ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusCreateAPIView(CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDetailByIdAPIView(RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"


class AllStatusByUserId(ListAPIView):
    serializer_class = StatusSerializer

    def get_queryset(self):
        user_id = self.kwargs["user"]
        return Status.objects.filter(user=user_id)


class StatusUpdateAPIView(UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusUpdateSerializer
    lookup_field = "id"


class StatusDeleteAPIView(DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"


### THE ABOVE CRUD OPERATION CAN BE DONE IN JUST TWO CLASS
### YOU NEED A BASE CLASS TO APPLY MIXIN
### STANDALONE MIXIN DONT WORK


## LIST AND POST
class StatusListPostView(ListAPIView, mixins.CreateModelMixin):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


## DETAIL UPDATE AND DELETE


class StatusDetailPutPatchDelete(
    RetrieveAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
