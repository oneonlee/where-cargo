from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import View
from datetime import date

from terminal.models import ContainerState

class terminal_yard(View):
    def get(self, request):
        # new_ContainerState=ContainerState()
        # new_ContainerState.container_number="HLBU803519"
        # new_ContainerState.resource_weight=19
        # new_ContainerState.state="LCL"
        # new_ContainerState.yard_location="3F"
        # new_ContainerState.booking_note="USN22F70142"
        # new_ContainerState.stack_location="3C 04-6"
        # new_ContainerState.start_time=date.today()
        # new_ContainerState.first_time=date.today()
        # new_ContainerState.second_time=date.today()
        # new_ContainerState.third_time=date.today()
        # new_ContainerState.complete_time=date.today()
        # new_ContainerState.save()
        terminal_yard=ContainerState.objects.values()
        return render(request, 'terminal/terminal_yard.html', context={'terminal_yard_list': list(terminal_yard)})