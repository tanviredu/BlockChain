from json                    import JSONDecoder
from django.http             import JsonResponse
from .serializer             import ContactSerializer
from rest_framework.parsers  import JSONParser
from rest_framework          import views,status
from rest_framework.response import Response


class ContactAPIView(views.APIView):
    serializer_class = ContactSerializer

    def post(self,request):
        try:
            print(request)
            data = JSONParser().parse(request)
            
            serializer = ContactSerializer(data = data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            res = {
                "result":"error",
                "message": "JSON decoding error",
            }
            return JsonResponse(res,status= 400)
        