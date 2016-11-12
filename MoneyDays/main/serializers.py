from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import UserContribution

User = get_user_model()


class ContributionHyperlink(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk_user': obj.user_id,
            'pk_contribution': obj.id
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, lookup_url_kwarg='pk_user', lookup_field='id',
                                               view_name='moneyuser-detail')

    class Meta:
        model = User
        fields = ('url', 'id', 'email', 'first_name', 'last_name', 'gender', 'birth_day')


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField()

    def validate(self, attrs):
        if attrs['password_confirm'] != attrs['password']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return super(UserRegistrationSerializer, self).validate(attrs)

    def create(self, validated_data):
        # Remove Field password_confirm, THIS FIELD DOESN'T EXISTS ON DB.
        del validated_data['password_confirm']
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

    def to_representation(self, instance):
        # Remove Field password_confirm
        del self._readable_fields[-1]
        # Remove Field password
        del self._readable_fields[-1]
        return super(UserRegistrationSerializer, self).to_representation(instance)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'gender', 'birth_day', 'password', 'password_confirm')


class UserContributionSerializer(serializers.HyperlinkedModelSerializer):
    url = ContributionHyperlink(read_only=True, view_name="contribution-detail")
    user = serializers.HyperlinkedRelatedField(read_only=True, lookup_field='id', lookup_url_kwarg='pk_user', view_name='moneyuser-detail')

    class Meta:
        model = UserContribution
        fields = ('url', 'txn_amount', 'balance', 'time')
