from django.contrib import admin
from .models import UrlSchema


class UrlSchemaAdmin(admin.ModelAdmin):
    list_display = ["long_url", "short_url"]

    class Meta:
        model = UrlSchema


admin.site.register(UrlSchema, UrlSchemaAdmin)
