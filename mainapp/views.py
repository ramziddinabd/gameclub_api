from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .pagination import CustomPagination

# Create your views here.

# List amaliyoti , apilar ruyhatini chiqarish GET REQUEST
class DeviceListApiView(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    pagination_class = CustomPagination
# Create amaliyoti , yangi apilar yaratish POST REQUEST
class DeviceCreateApiView(generics.CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer



# List amaliyoti , apilar ruyhatini chiqarish GET REQUEST
class GamerListApiView(generics.ListAPIView):
    queryset = Gamer.objects.all()
    serializer_class = GamerSerializer
    pagination_class = CustomPagination
# Create amaliyoti , yangi apilar yaratish POST REQUEST
class GamerCreateApiView(generics.CreateAPIView):
    queryset = Gamer.objects.all()
    serializer_class = GamerSerializer



# List amaliyoti , apilar ruyhatini chiqarish GET REQUEST
class RentedDeviceListApiView(generics.ListAPIView):
    queryset = RentedDevice.objects.all()
    serializer_class = RentedDeviceSerializer
    pagination_class = CustomPagination
# Create amaliyoti , yangi apilar yaratish POST REQUEST
class RentedDeviceCreateApiView(generics.CreateAPIView):
    queryset = RentedDevice.objects.all()
    serializer_class = RentedDeviceSerializer

