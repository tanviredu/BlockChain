from django.contrib import admin
from API.models import UserProfile, Ingredient, CustomerDetail, Order


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["email", "is_active", "is_staff"]

    class Meta:
        model = UserProfile


class IngredientAdmin(admin.ModelAdmin):
    list_display = ["salad", "cheese", "meat"]

    class Meta:
        model = Ingredient


class CustomerDetailAdmin(admin.ModelAdmin):
    list_display = ["deliveryAddress", "phone", "paymentType"]

    class Meta:
        model = CustomerDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "price", "orderTime"]

    class Meta:
        model = Order


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(CustomerDetail, CustomerDetailAdmin)
