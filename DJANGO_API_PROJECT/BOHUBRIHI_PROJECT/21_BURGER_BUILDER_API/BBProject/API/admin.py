from django.contrib import admin
from API.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["email", "is_active", "is_staff"]

    class Meta:
        model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)
