from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Photos


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'
