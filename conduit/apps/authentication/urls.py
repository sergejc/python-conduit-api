from django.conf.urls import url
from .views import RegistratinAPIView

urlpatterns = [
    url(r'^users/?$', RegistratinAPIView.as_view()),
]
