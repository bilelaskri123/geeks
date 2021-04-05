from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi
from .api import ListUserAPIView
from .api import DeleteUserAPIView
from .api import UpdateUserAPIView
from .api import UserById
urlpatterns = [
      path('api/register', RegisterApi.as_view()),
      path('api/users/<int:pk>', UserById.as_view()),
      path('api/users', ListUserAPIView.as_view()),
      path("api/update/<int:pk>", UpdateUserAPIView.as_view()),
      path("api/delete/<int:pk>", DeleteUserAPIView.as_view(), name="delete_user")
]