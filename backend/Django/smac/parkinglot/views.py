from django.shortcuts import render
from django.views import View
from parkingapp.models import ParkingState
# Create your views here.

class Parkinglot_car(View):
    def get(self, request):
        parking_data=ParkingState.objects.values()
        parking_list=list(parking_data)
        parking_list=parking_list[0:4]
        return render(request, 'parkinglot/parking_car.html', context={'parking_list': list(parking_list)})

class Parkinglot_truck(View):
    def get(self, request):
        parking_data=ParkingState.objects.values()
        parking_list=list(parking_data)
        parking_list=parking_list[4:8]
        return render(request, 'parkinglot/parking_truck.html', context={'parking_list': list(parking_list)})