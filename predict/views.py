from django.http.response import HttpResponse
from django.shortcuts import render
from .ml_controller import ML_Controller


# Create your views here.

def home(request):

    return render(request, 'predict/home.html', {})