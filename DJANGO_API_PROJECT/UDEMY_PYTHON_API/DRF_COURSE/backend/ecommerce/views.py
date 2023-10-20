from json                       import JSONDecodeError
from django.http                import JsonResponse
from .serializer                import ItemSerializer,OrderSerializer
from .models                    import Item, Order
from rest_framework.parsers     import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework             import viewsets,status
from rest_framework.response    import Response
from rest_framework.mixins      import ListModelMixin,UpdateModelMixin,RetrieveModelMixin


class ItemViewSet(ListModelMixin,RetrieveModelMixin,viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = Item.objects.all()
    serializer_class   = ItemSerializer

class OrderViewSet(ListModelMixin,RetrieveModelMixin,UpdateModelMixin,viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class   = OrderSerializer

    def get_queryset(self):
        ## modify the get method
        ## depending how this will react
        ## to get request
        user = self.request.user
        return Order.objects.filter(user = user)
    
    def create(self,request):
        try:

            data       = JSONParser().parse(request)
            serializer = OrderSerializer(data = data)
            if serializer.is_valid(raise_exception=True):

                ## this 
                item   = Item.objects.get(pk=data["item"])
                order  = item.place_order(request.user,data["quantity"])
                return Response(OrderSerializer(order).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({
                "result":"error",
                "message":"Json Decoding error"
            },status = 400)