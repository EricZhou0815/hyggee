from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer,TripSerializer,UserProfileSerializer
from .models import Trip,UserProfile
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset=Trip.objects.all()
    serializer_class=TripSerializer