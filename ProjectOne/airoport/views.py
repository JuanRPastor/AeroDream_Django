from django.shortcuts import render
from airoport.models import Route

# Create your views here.


def index(request):
    routes = Route.objects.all()
    return render(request, "index.html", {"routes": routes})
