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
    return [pie, n]

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
    return [pie, n]

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
    return [pie, n]

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
    return [pie, n]

print("The near pi value for basel function is: " + str(basel(precision)[0]) + " and the number of steps taken is " + str(basel(precision)[1]))
print("The near pi value for taylor function is: " + str(taylor(precision)[0]) + " and the number of steps taken is " + str(taylor(precision)[1]))
print("The near pi value for wallis function is: " + str(wallis(precision)[0]) + " and the number of steps taken is " + str(wallis(precision)[1]))
print("The near pi value for spigot function is: " + str(spigot(precision)[0]) + " and the number of steps taken is " + str(spigot(precision)[1]))

algorithms=[]
output = []
def takeSecond(elem):
    return elem[1]

def race(precision, algorithms):
    for i in range(4):
        algorithm_input = str(input("Enter name of functions (enter 'quit' to end): "))
        algorithms.append(algorithm_input)
        if algorithm_input == 'quit':
            break
    for i in range(len(algorithms)):
        if 'basel' == algorithms[i]:
            output.append(basel(precision))
            del output[i][0]
            output[i].insert(0, i+1)
        elif 'taylor' == algorithms[i]:
            output.append(taylor(precision))
            del output[i][0]
            output[i].insert(0, i+1)
        elif 'wallis' == algorithms[i]:
            output.append(wallis(precision))
            del output[i][0]
            output[i].insert(0, i+1)
        elif 'spigot' == algorithms[i]:
            output.append(spigot(precision))
            del output[i][0]
            output[i].insert(0, i+1)
    output.sort(key=takeSecond)
    return output
print(race(precision, algorithms))

def print_results(output):
    for i in range(len(output)):
        print("Algorithm " + str(output[i][0]) + " finished in " + str(output[i][1]) + " steps.")
print_results(output)
