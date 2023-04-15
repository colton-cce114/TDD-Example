from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def calculate(request):
    weight = float(request.GET['weight'])
    height = float(request.GET['height'])

    res = getBMI(weight, height)

    return render(request, 'calculate.html', {'bmi':getBMI(weight, height), 'category':categorizeBMI(getBMI(weight, height))})

#Helper functions
def multiplyFunc(a, b): #There is a math function for this but I don't feel like using it
    return a*b

def convertHeight(a):
    return round(multiplyFunc(a,0.025), 3)

def squareFunc(a):
    return round(multiplyFunc(a,a), 6)

def divideFunc(a, b):
    return round((a/b), 1)

def getBMI(a, b):
    weight = round(multiplyFunc(a, 0.45), 2)
    height = convertHeight(b)
    return round((weight/squareFunc(height)), 1)

def categorizeBMI(a):
    if a < 18.5: return 'underweight'
    elif 18.5 <= a <= 24.9: return 'normal weight'
    elif 25 <= a <= 29.9: return 'overweight'
    elif a >= 30: return 'obese'