from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserContribution

User = get_user_model()


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
    class Meta:
        model = UserContribution
        fields = ('url', 'txn_amount', 'balance', 'time')
