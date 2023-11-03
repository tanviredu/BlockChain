from django.urls             import path
from .views                  import UrlCreateAPIView
urlpatterns = [
    path("short/",UrlCreateAPIView.as_view()),
]
