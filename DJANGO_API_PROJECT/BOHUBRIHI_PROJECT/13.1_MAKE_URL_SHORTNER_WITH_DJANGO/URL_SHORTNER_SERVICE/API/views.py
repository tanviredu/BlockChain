from .models        import UrlSchema
from .serializers   import UrlSchemaGetSerializer,UrlSchemaPostSerializer
from rest_framework import generics
from rest_framework import views
from rest_framework import status
from rest_framework.response   import Response
from rest_framework.decorators import api_view
from rest_framework.parsers    import JSONParser
import random
import string


def get_random_string():
    letters    = string.ascii_uppercase
    result_str = "".join(random.choice(letters) for item in range(4))
    return result_str 





class UrlCreateAPIView(generics.CreateAPIView):
    queryset          = UrlSchema.objects.all()
    serializer_class  = UrlSchemaPostSerializer

    def create(self,request,*args,**kwargs):
        base_url = "127.0.0.1:8000"
        long_url   = request.data.get("long_url")
        print("[*] LONG URL : {}".format(long_url))
        data = UrlSchema.objects.filter(long_url=long_url)
        #return Response({"detail":"message"})
        #return super(UrlCreateAPIView, self).create(request, *args, **kwargs)
        if not data.exists():
            short_code = get_random_string()
            short_url  = base_url + "/"+short_code
            print("[*] SHORT URL : {}".format(short_url))
            return Response({"data":short_url})
        return Response({"data":"problem"})




