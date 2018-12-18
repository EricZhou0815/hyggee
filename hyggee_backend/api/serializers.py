
from django.contrib.auth.models import User, Group
from .models import Trip,UserProfile
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('pk','url','username','email','groups')
        #fields='__all__'

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=('pk','url','name')


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Trip
        fields='__all__'
        include='pk'