from rest_framework import serializers
from .models        import UrlSchema

class UrlSchemaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UrlSchema
        fields = ["long_url"] 

class UrlSchemaGetSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UrlSchema
        fields = ["id","long_url","short_url"]
         