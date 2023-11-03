from django.urls import path
from rest_framework import routers
from .views import (
    StatusAPIView,
    StatusListAPIView,
    StatusCreateAPIView,
    StatusDetailByIdAPIView,
    AllStatusByUserId,
    StatusUpdateAPIView,
    StatusDeleteAPIView,
    StatusListPostView,
    StatusDetailPutPatchDelete,
    GenericListPostView,
    GenericRetUpdateDestroy,
    StatusViewSet,
)

router = routers.DefaultRouter()
router.register(r"statusV4", StatusViewSet, basename="status")

urlpatterns = [
    path("statusV3/", GenericListPostView.as_view()),
    path("statusV3/<id>/", GenericRetUpdateDestroy.as_view()),
    ##
    path("statusV2/", StatusListPostView.as_view()),
    path("statusV2/<id>", StatusDetailPutPatchDelete.as_view()),
    ##
    path("statusV1/", StatusAPIView.as_view()),
    path("statusV1/list/", StatusListAPIView.as_view()),
    path("statusV1/create/", StatusCreateAPIView.as_view()),
    path("statusV1/detail/<id>/", StatusDetailByIdAPIView.as_view()),
    path("statusV1/detail/user/<user>/", AllStatusByUserId.as_view()),
    path("statusV1/update/<id>/", StatusUpdateAPIView.as_view()),
    path("statusV1/delete/<id>/", StatusDeleteAPIView.as_view()),
]

urlpatterns += router.urls
