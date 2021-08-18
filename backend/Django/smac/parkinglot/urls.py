from django.urls import path

from parkinglot.views import Parkinglot_car,Parkinglot_truck

app_name = "parkinglot"

urlpatterns = [
    path('car/', Parkinglot_car.as_view(), name="car"),
    path('truck/', Parkinglot_truck.as_view(), name="car")
]