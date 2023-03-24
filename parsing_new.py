from math import pow

numbers = '1234567890'
symbols = '+-*/^()'
def tokenization(expr):
    new_expr = list(expr)
    count = new_expr.count(' ')
    i = 0
    while i != count:
        new_expr.remove(" ")
        i += 1
    first_mark = 0
    second_mark = 0
    count2 = new_expr.count('.')
    n = 0
    while n != count2:
        for j in range(len(new_expr)):
            if new_expr[j] == '.':
                k = j-1
                while new_expr[k] in numbers:
                    first_mark = k
                    k -= 1
                l = j+1
                while new_expr[l] in numbers:
                    second_mark = l+1
                    l += 1
                new_expr[first_mark:second_mark] = [''.join(new_expr[first_mark:second_mark])]
                n += 1
                break
    for i in range(len(new_expr)):
        if new_expr[i] not in symbols:
            new_expr[i] = float(new_expr[i])
    return(new_expr)

def has_precedence(op1, op2):
    high = '^'
    middle = '*/'
    low = '+-'
    if op1 in high and op2 in middle:
        return True
    elif op1 in high and op2 in low:
        return True
    elif op1 in middle and op2 in low:
        return True
    else:
        return False

def simple_evaluation(tokens):
    count_high, count_middle, count_low, high, middle, low = 0,0,0,0,0,0
    for i in range(len(tokens)):
        if str(tokens[i]) in symbols:
            if tokens[i] == '^':
                count_high += 1
            elif tokens[i] == '*' or tokens[i] == '/':
                count_middle += 1
            elif tokens[i] == '+' or tokens[i] == '-':
                count_low += 1
    while high != count_high:
        for i in range(len(tokens)):
            if tokens[i] == "^":
                temp_value = tokens[i-1]**tokens[i+1]
                tokens[i-1:i+2] = []
                tokens.insert(i-1, float(temp_value))
                high += 1
                break
    while middle != count_middle:
        for i in range(len(tokens)):
            if tokens[i] == "*":
                temp_value = tokens[i-1]*tokens[i+1]
                tokens[i-1:i+2] = []
                tokens.insert(i-1, float(temp_value))
                middle += 1
                break
            elif tokens[i] == "/":
                temp_value = tokens[i-1]/tokens[i+1]
                tokens[i-1:i+2] = []
                tokens.insert(i-1, float(temp_value))
                middle += 1
                break
    while low != count_low:
        for i in range(len(tokens)):
            if tokens[i] == "+":
                temp_value = tokens[i-1]+tokens[i+1]
                tokens[i-1:i+2] = []
                tokens.insert(i-1, float(temp_value))
                low += 1
                break
            elif tokens[i] == "-":
                temp_value = tokens[i-1]-tokens[i+1]
                tokens[i-1:i+2] = []
                tokens.insert(i-1, float(temp_value))
                low += 1
                break
    return(tokens[0])

def complex_evaluation(tokens):
    count_high, count_middle,count_low, count_brackets, number_of_brackets = 0,0,0,0,0
    for i in range(len(tokens)):
        if str(tokens[i]) in symbols:
            if tokens[i] == '^':
                count_high += 1
            elif tokens[i] == '*' or tokens[i] == '/':
                count_middle += 1
            elif tokens[i] == '+' or tokens[i] == '-':
                count_low += 1
            elif tokens[i] == '(':
                count_brackets += 1
    while number_of_brackets != count_brackets:
        if "(" not in tokens:
            break
        for k in range(len(tokens)):
            if tokens[k] == "(":
                for j in range(k+1, len(tokens)):
                    if tokens[j] == ")":
                        temp_value = simple_evaluation(tokens[k+1:j])
                        tokens[k:j+1] = []
                        number_of_brackets += 1
                        tokens.insert(k, float(temp_value))
                        break
                    elif tokens[j] == "(":
                        count1, count2 = 1, 0
                        for n in range(j+1, len(tokens)):
                            if tokens[n] == "(":
                                count1 += 1
                            elif tokens[n] == ")":
                                count2 += 1
                                if count1 == count2:
                                    temp_value = complex_evaluation(tokens[j:n+1])
                                    tokens[j:n+1] = []
                                    number_of_brackets += 1
                                    tokens.insert(j, temp_value)
                                    break
                else:
                    continue
                break
    return(simple_evaluation(tokens))

def evaluation(string):
    list1 = tokenization(string)
    return complex_evaluation(list1)
    
print(complex_evaluation(["(", 2, "-", 7, ")", "*", 4, "^", "(", 2, "+", 1, ")"]))
#print(evaluation("(2-7) * 4^(2+1)"))
