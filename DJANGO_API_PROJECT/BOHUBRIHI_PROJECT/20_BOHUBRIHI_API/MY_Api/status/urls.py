from django.urls import path
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
)

urlpatterns = [
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
