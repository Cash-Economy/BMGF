from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .permissions import IsOwnerOrStaff, NotAllowRegisterAccountToAuthenticated
from .serializers import UserSerializer, UserRegistrationSerializer

User = get_user_model()


class UserList(generics.ListCreateAPIView):
    """
    Only the Admin sees all users, Only allow registration to Anonymous (not logged in) users
    """
    permission_classes = (permissions.AllowAny, NotAllowRegisterAccountToAuthenticated)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserRegistrationSerializer
        else:
            return UserSerializer

    def get_queryset(self):
        # print "User LIST"
        if self.request.user.is_staff:
            return User.objects.all().order_by('-date_joined')
        else:
            return User.objects.filter(id=self.request.user.id)


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Only an Admin or the User it Self can Retrieve or modify his/her data.
    """
    lookup_url_kwarg = 'pk_user'
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrStaff,)

    def get_object(self):
        if self.kwargs['pk_user'] == "self":
            self.kwargs['pk_user'] = str(self.request.user.id)
        return super(UserDetail, self).get_object()



@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        # 'measurements': reverse('measurement-list', request=request, format=format)
    })
