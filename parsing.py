numbers = '1234567890'
symbols = '+-*/^()'
def tokenization(expr):
    new_expr = list(expr)
    #this separates every characters in the string into individual item in a list
    count = new_expr.count(' ')
    i = 0
    while i != count:
        new_expr.remove(" ")
        i += 1
    #this gets rid of all the blank spaces in the list
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
            #this part joins the number separated by the decimals
            #this is done by first counting the number of decimal places
            #then measuring the indexes of numbers before and after the decimal
            #then join them using join function and look for next decimal
    a = True
    while a:
        for i in range(len(new_expr)):
            if a == False:
                break
            if new_expr[i] in numbers:
                mark = i
                if new_expr[mark+1] in numbers:
                    while new_expr[mark+1] in numbers:
                        new_mark = mark+1
                        mark += 1
                        if mark == len(new_expr)-1:
                            if new_expr[mark] in numbers:
                                new_expr[i:new_mark+1] = [''.join(new_expr[i:new_mark+1])]    
                                a = False
                                break
                            #similar to the decimal function above, this finds the
                            #first number then find the index of the last number in
                            #a row, then join them together
                    else:
                        new_expr[i:new_mark+1] = [''.join(new_expr[i:new_mark+1])]
                        break
            elif i == len(new_expr) - 1:
                a = False
                break #if it is the end of the list, break the whole loop
            #the while loop allow for the resetting of the for loop so the
            #len(new_expr) can be newly measured, by doing this repeatedly,
            #it will confirm with new (possibly shorter) length of list 
            #as some of them are combined to make one number
    for i in range(len(new_expr)):
        if new_expr[i] not in symbols:
            new_expr[i] = float(new_expr[i]) #changes each number in the list to float numbers
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
                #counting the number of symbols and separating them into precedences
    while high != count_high:
        for i in range(len(tokens)):
            if tokens[i] == "^":
                temp_value = tokens[i-1]**tokens[i+1]
                tokens[i-1:i+2] = []
                tokens.insert(i-1, float(temp_value))
                high += 1
                break
            #because ^ has highest precedence, it occurs first and loop to find ^ in list
            #if found, replace the the value in front and after with calculation of temp value
            #then replace the numbers with temp value
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
            #similar to ^, * and / have same precedence and but lower than ^
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
            #list the number of symbols and separate them
    while number_of_brackets != count_brackets:
        if "(" not in tokens:
            break #if there are no more brackets, break the loop and let simple evaluation occur to calculate
        for k in range(len(tokens)):
            if tokens[k] == "(":
                for j in range(k+1, len(tokens)):
                    if tokens[j] == ")":
                        temp_value = simple_evaluation(tokens[k+1:j])
                        tokens[k:j+1] = []
                        number_of_brackets += 1
                        tokens.insert(k, float(temp_value))
                        break
                    #in the case of normal brackets, the elements are replaced with
                    #calculation of the value between the brackets
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
                    #in the case of nested brackets, we count the number of open brackets
                    #and close brackets. once they are the same, it means the outside
                    #brackets has to execute and calculate what is inside
                    #by using recursion we can calculate the brackets inside first
                    #then give back the value so the outside brackets can be calculated
                else:
                    continue
                break
    return(simple_evaluation(tokens)) #in the end there may be still some calculation left to do
#so use simple eval to calculate final result

def evaluation(string):
    list1 = tokenization(string)
    return complex_evaluation(list1)
#turn string into correct format so it can be calculated by complex eval

print(evaluation("((5+1*4))"))
