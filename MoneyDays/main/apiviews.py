from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from twilio.rest import TwilioRestClient

from MoneyDays.keys import ACCOUNT_SID, AUTH_TOKEN
from .models import UserContribution, UserPointMovement
from .permissions import IsOwnerOrStaff, NotAllowRegisterAccountToAuthenticated
from .serializers import UserSerializer, UserRegistrationSerializer, UserContributionSerializer,UserContributionCreationSerializer
from .permissions import IsOwnerOrStaff, NotAllowRegisterAccountToAuthenticated
from .serializers import UserSerializer, UserRegistrationSerializer
from .transaction_utils import make_suggestions

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


class UserContributionList(generics.ListCreateAPIView):
    """
    Only an Admin or the Owner of the measurements can list them
    or create them.
    """
    permission_classes = (IsOwnerOrStaff,)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserContributionCreationSerializer
        else:
            return UserContributionSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('pk_user')
        # print "User Measurement LIST"
        # print "PK USER:" + user_id
        return UserContribution.objects.filter(user=user_id).order_by("-time")

    def perform_create(self, serializer):
        amount = serializer.validated_data.get('txn_amount')

        #TWILIO API SMS CONFIRMATION
        contrib = UserContribution(user=self.request.user, txn_amount=float(amount))
        contrib.save()

        contrib = UserPointMovement(user=self.request.user, txn_amount=0)
        contrib.save()

        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

        client.messages.create(
            to=self.request.user.phone_number,
            from_="+16072755081",
            body="Congratulations " + self.request.user.first_name + "! You have made a deposit of: " + str(amount) + "$",
        )

        #TODO TRIGGER BANK TRANSACTION

        #TODO TRIGGER RECOMMENDED AMOUNT RECALCULATION

        #FINALLY SAVE TRANSACTION TO DATABASE
        serializer.save(user=self.request.user, txn_amount=amount)


class UserContributionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Only an Admin or the Owner of the measurements can modify, retrieve or delete them.
    """
    serializer_class = UserContributionSerializer
    permission_classes = (IsOwnerOrStaff,)

    def get_queryset(self):
        user_id = self.kwargs.get('pk_user')
        contribution_id = self.kwargs.get('pk_contribution')
        return UserContribution.objects.filter(user=user_id, id=contribution_id)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        return obj


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('moneyuser-list', request=request, format=format),
        # 'measurements': reverse('measurement-list', request=request, format=format)
    })


@api_view(('GET',))
def get_user_saving_recommendations(request, pk_user):
    d = {'suggestion': make_suggestions(int(pk_user))}
    return Response(data=d)
