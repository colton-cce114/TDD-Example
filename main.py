#This code is disgusting

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

print("Welcom to the BMI Calculator!")
print("I made this late at night so make")
print("SURE you're entering correct values.")

while True:
    weight = input("Weight(pounds): ")
    height = input("Height(inches): ")

    print("You're BMI is a smooth ", getBMI(weight, height), "making you ", categorizeBMI(getBMI(weight, height)))

    if (input("Continue? (y/n): ") != 'y'): return False
