from math import pi,sqrt
precision = float(input("Enter the precision number: "))   
def basel(precision):
    pie = 0
    j = 1
    term = 1/j**2
    n = 0
    while abs(pi-pie)> precision:
        pie = sqrt(6*term)
        j += 1
        n += 1
        term += 1/j**2
    return ('Basel: ', pie,n)


def taylor(precision):
    pie = 0
    j = 1
    term = 1/j
    k = 1
    n = 0
    while abs(pi-pie)> precision:
        pie = 4*(term)
        j += 2
        k += 1
        n += 1
        if k%2==0:
            term -= 1/j
        else:
            term += 1/j
    return ('Taylor: ', pie, n)

def wallis(precision):
    pie = 0
    j = 2
    term = (j*j)/((j-1)*(j+1))
    n = 0
    while abs(pi-pie)> precision:
        pie = 2 * (term)
        j += 2
        n += 1
        term *= (j*j)/((j-1)*(j+1))
    return ('Wallis: ', pie, n)

def spigot(precision):
    pie = 0
    i = 1 #counter
    j = 1 #denominator number
    k = 1 #numerator number
    n = 0
    term = k/j
    bigger_term = 0
    while abs(pi - pie) > precision:
        bigger_term += term
        pie = 2 * (bigger_term)
        j += 2
        n += 1
        if j > 3:
            k += 1
            term *= k/j
        else:
            term *= k/j
    return ('Spigot: ', pie, n)
print(basel(precision))
print(taylor(precision))
print(wallis(precision))
print(spigot(precision))

algorithm_input = str(input("enter name of functions: "))
algorithms=[]
algorithms.append(algorithm_input)
def race(precision, algorithms):
    for i in range(len(algorithms)):
        if 'basel' == algorithms[i]:
            return print(basel(precision))
        elif 'taylor' == algorithms[i]:
            return print(taylor(precision))
        elif 'wallis' == algorithms[i]:
            return print(wallis(precision))
        elif 'spigot' == algorithms[i]:
            return print(spigot(precision))
        
print(race(precision, algorithms))
