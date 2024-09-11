from django.shortcuts import render


def home(request):
    return render(request, 'converter/base.html')



def convert_length(value, from_unit, to_unit):
    units = {
        'centimeter': 1e-2,
        'meter': 1,
        'kilometer': 1e3,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.344
    }
    meters = value * units[from_unit]
    return meters / units[to_unit]

def convert_weight(value, from_unit, to_unit):
    units = {
        'gram': 1,
        'kilogram': 1e3,
        'pound': 453.592
    }
    grams = value * units[from_unit]
    return grams / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        return value
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        return value
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        return value



def length_converter(request):
    result = None
    return render(request, 'converter/length.html', {'result': result})

def weight_converter(request):
    result = None
    return render(request, 'converter/weight.html', {'result': result})

def temperature_converter(request):
    result = None
    return render(request, 'converter/temperature.html', {'result': result})