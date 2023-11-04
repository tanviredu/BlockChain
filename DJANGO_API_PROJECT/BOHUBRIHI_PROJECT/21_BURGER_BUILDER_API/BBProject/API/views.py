from rest_framework.viewsets import ModelViewSet
from API.models import UserProfile
from API.serializers import UserProfileSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
