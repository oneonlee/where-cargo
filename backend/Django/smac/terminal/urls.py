from django.urls import path

from terminal.views import terminal_yard

app_name = "terminal"

urlpatterns = [
    path('yard/', terminal_yard.as_view(), name='yard')
]