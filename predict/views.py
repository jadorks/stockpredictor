from django.http.response import HttpResponse
from django.shortcuts import render
from tensorflow.python.eager.context import context
from .ml_controller import ML_Controller
import re


# Create your views here.

def home(request):
    return render(request, 'predict/home.html', {})

def details(request, ticker):
    mlc = ML_Controller(ticker)
    res = mlc.magic()
    pred = str(res[0])


    context = {'ticker': ticker, 'predictions': re.sub('[^A-Za-z0-9.]+', '', pred), 'img':res[1]}

    return render(request, 'predict/content.html', context)