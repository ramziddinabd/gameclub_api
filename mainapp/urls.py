from django.urls import path
from . import views


urlpatterns = [
    path('list-device-api-view', views.DeviceListApiView.as_view()),
    path('create-device-api', views.DeviceCreateApiView.as_view()),

    path('list-gamer-api-view', views.GamerListApiView.as_view()),
    path('create-gamer-api', views.GamerCreateApiView.as_view()),

    path('list-rdevice-api-view', views.RentedDeviceListApiView.as_view()),
    path('create-rdevice-api', views.RentedDeviceCreateApiView.as_view()),
]
