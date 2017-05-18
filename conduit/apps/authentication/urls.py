from django.conf.urls import url
from .views import (LoginAPIView, RegistratinAPIView, UserRetrieveUpdateAPIView)

urlpatterns = [
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
]
