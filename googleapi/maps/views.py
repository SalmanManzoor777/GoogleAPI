from django.shortcuts import render
from . import views
from django.urls import path,URLPattern

# Create your views here.
def index(request):
    mapbox_access_token = 'pk.eyJ1IjoiaGFpZGVyYWxpMTIiLCJhIjoiY2tnNTE2dWtlMHB3MTJwbm5iM2hlM2dqdyJ9.b1WtGGr-9yXlfBc_9WBjZw'
    return render(request, 'index.html', {'mapbox_access_token':mapbox_access_token})
