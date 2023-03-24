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
    a = True
    while a:
        for i in range(len(new_expr)):
            if a == False:
                break
            if new_expr[i] in numbers:
                mark = i
                while new_expr[mark+1] in numbers:
                    new_mark = mark+1
                    mark += 1
                    if mark == len(new_expr)-1:
                        if new_expr[mark] in numbers:
                            new_expr[i:new_mark+1] = [''.join(new_expr[i:new_mark+1])]    
                            a = False
                            break
                else:
                    new_expr[i:new_mark+1] = [''.join(new_expr[i:new_mark+1])]
                    break
    for i in range(len(new_expr)):
        if new_expr[i] not in symbols:
            new_expr[i] = float(new_expr[i])
    return(new_expr)
    
print(tokenization("43-34"))
