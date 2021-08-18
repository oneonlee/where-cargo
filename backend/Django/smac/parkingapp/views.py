import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

#@method_decorator(csrf_exempt, name='dispatch')
from parkingapp.models import ParkingState

class ParkingView(View):
    def post(self, request):
        data = json.loads(request.body)
        print(type(data))
        for i in data:
            if ParkingState.objects.filter(location=i).exists()==False:
                Parking_data=ParkingState.objects.create(
                    location=i,
                    state=str(data[i])
                )
                Parking_data.save()
            else:
                Parking_data=ParkingState.objects.get(location=i)
                if Parking_data.state != str(data[i]):
                    Parking_data.state = str(data[i])
                    Parking_data.save()
        return HttpResponse(status=200)
    def get(self, request):
        Parking_data=ParkingState.objects.values()
        print(type(Parking_data[0]["location"]))
        print(type(Parking_data))
        Parking_list=list(Parking_data)
        print(Parking_list[0:1])
        return JsonResponse({'parks': list(Parking_data)}, status=200)