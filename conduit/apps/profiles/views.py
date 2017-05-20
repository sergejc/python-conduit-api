from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer

class ProfileRetrieveAPIView(RetrieveAPIView):
    permissions_class = (AllowAny,)
    queryset = Profile.objects.select_related('user')
    renderer_class = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def retrieve(self, request, username, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            # We use the `select_related` method to avoid making unnecessary
            # database calls.
            profile = Profile.objects.select_related('user').get(
                user__usrname=username
            )
            profile = self.queryset.get(user__usrname=username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username does not exist')

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

