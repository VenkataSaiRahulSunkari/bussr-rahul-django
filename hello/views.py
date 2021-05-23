from django.http import HttpResponse
import socket
from datetime import date

host_name = socket.gethostname()
today = date.today()

def index(request):
    return HttpResponse("Hello World! I am running on " + str(host_name) + " and today is " + str(today))
