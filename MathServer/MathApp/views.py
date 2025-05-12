from django.shortcuts import render

def calculate_power(request):
    if request.method == 'POST':
        intensity = float(request.POST.get('intensity', 0))
        resistance = float(request.POST.get('resistance', 0))
        power = intensity * intensity * resistance
        return render(request, 'power_calculator.html', {'power': power})
    return render(request, 'power_calculator.html')