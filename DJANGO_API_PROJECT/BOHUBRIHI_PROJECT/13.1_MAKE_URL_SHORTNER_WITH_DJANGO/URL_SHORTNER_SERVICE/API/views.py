from .models import UrlSchema
from .serializers import UrlSchemaGetSerializer, UrlSchemaPostSerializer
from rest_framework import generics
from rest_framework import views
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import HttpResponseRedirect
from API.Utils.Helper import get_random_string






class UrlGetAPIView(generics.RetrieveAPIView):
    queryset = UrlSchema.objects.all()
    serializer_class = UrlSchemaGetSerializer
    lookup_field = "url_code"

    def get(self, request, *args, **kwargs):
        short_url_param = str(self.kwargs.get("url_code"))
        existing_entry = UrlSchema.objects.filter(url_code=short_url_param).first()
        if existing_entry:
            long_url = str(existing_entry.long_url)
            id = str(existing_entry.id)
            short_url = str(existing_entry.short_url)
            data = {"id": id, "short_url": short_url, "long_url": long_url}
            return Response(data)
        else:
            data = {"info": "No Entry"}
            return Response(data,status=status.HTTP_200_OK)


class UrlCreateAPIView(generics.CreateAPIView):
    queryset = UrlSchema.objects.all()
    serializer_class = UrlSchemaPostSerializer

    def create(self, request, *args, **kwargs):
        base_url = "127.0.0.1:8000"
        long_url = request.data.get("long_url")
        print("[*] LONG URL : {}".format(long_url))
        data = UrlSchema.objects.filter(long_url=long_url).first()
        # return Response({"detail":"message"})
        # return super(UrlCreateAPIView, self).create(request, *args, **kwargs)
        if not data:
            short_code = get_random_string()
            short_url = base_url + "/apiV1/" + short_code
            print("[*] SHORT URL : {}".format(short_url))
            ## save in the database
            new_entry = UrlSchema(
                url_code=short_code, long_url=long_url, short_url=short_url
            )
            new_entry.save()
            long_url = str(new_entry.long_url)
            short_url = str(new_entry.short_url)

            respose = {
                "id": str(new_entry.id),
                "long_url": long_url,
                "short_url": short_url,
            }

            return Response(respose,status=status.HTTP_201_CREATED)

        ## if exists
        print("[*] ", data.long_url)
        print("[*] ", data.short_url)
        long_url = str(data.long_url)
        short_url = str(data.short_url)

        respose = {"id": str(data.id), "long_url": long_url, "short_url": short_url}
        return Response(respose,status=status.HTTP_200_OK)


# views.py
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import UrlSchema
# from .serializers import UrlSchemaSerializer

# class UrlCreateAPIView(APIView):
#    def post(self, request, format=None):
#        long_url = request.data.get('long_url')

# Check if an entry with the given long_url already exists
#        existing_entry = UrlSchema.objects.filter(long_url=long_url).first()

#        if existing_entry:
# Return the existing short_url
#            serializer = UrlSchemaSerializer(existing_entry)
#            return Response(serializer.data)

# If no existing entry, generate a short_url and create a new entry
# You need to implement the logic to generate short URLs here
# For example, you can use a library like shortuuid
# After generating the short URL, save it to the database
# and return it in the response
# Ensure that you handle URL generation and uniqueness properly

# For simplicity, let's assume you generate a short URL like this:
# short_url = "http://example.com/abc123"

# Create a new entry
#        new_entry = UrlSchema(long_url=long_url, short_url=short_url)
#        new_entry.save()

#        serializer = UrlSchemaSerializer(new_entry)
#        return Response(serializer.data, status=status.HTTP_201_CREATED)
