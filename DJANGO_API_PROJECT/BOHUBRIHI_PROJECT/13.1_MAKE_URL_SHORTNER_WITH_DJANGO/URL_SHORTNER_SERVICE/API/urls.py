from django.urls import path
from .views import UrlCreateAPIView, UrlGetAPIView

urlpatterns = [
    path("short/", UrlCreateAPIView.as_view()),
    path("<str:url_code>/", UrlGetAPIView.as_view()),
]
