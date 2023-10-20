from django.urls    import path
from django.contrib import admin
from rest_framework import routers
from core           import views as core_views
from ecommerce      import views as ecommerce_views
from rest_framework.authtoken.views import obtain_auth_token

router      = routers.DefaultRouter()
router.register('item',ecommerce_views.ItemViewSet,basename='item')
router.register("order",ecommerce_views.OrderViewSet,basename="order")
urlpatterns = router.urls
urlpatterns += [
    path('admin/'  , admin.site.urls),
    path('contact/', core_views.ContactAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]
