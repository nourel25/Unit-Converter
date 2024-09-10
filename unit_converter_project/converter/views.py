from django.shortcuts import render


def home(request):
    return render(request, 'converter/base.html')


def length_converter(request):
    result = None
    return render(request, 'converter/length.html', {'result': result})

def weight_converter(request):
    result = None
    return render(request, 'converter/weight.html', {'result': result})

def temperature_converter(request):
    result = None
    return render(request, 'converter/temperature.html', {'result': result})