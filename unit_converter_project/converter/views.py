from django.shortcuts import render


def home(request):
    return render(request, 'converter/base.html')


def length_converter(request):
    return render(request, 'converter/length.html')

def weight_converter(request):
    return render(request, 'converter/weight.html')

def temperature_converter(request):
    return render(request, 'converter/temperature.html')