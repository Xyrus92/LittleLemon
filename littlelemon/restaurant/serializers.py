from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class MenuSerializer(serializers.ModelSerializer):
    class Meta():
        model = Menu
        fields = ['id','title','price','inventory']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Booking
        fields = '__all__'