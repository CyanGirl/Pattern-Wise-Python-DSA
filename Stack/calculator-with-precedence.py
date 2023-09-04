'''
Implement basic calculator, eval this string expression. 
The operators are + , - , * , ^ where ^ (exponent) operator has more precedence than * and * operator has more precedence than + and -
Examples:
23^2 = 18
1+23 = 7
4 * 3 + 2  ^2 ^2 = 28
'''
    


def calculate(expression):
    preceds={"-":1,"+":1,"*":2,"^":3}

    signs=[]
    queue=[]
    curnum=0
    for i in range(len(expression)):
        if expression[i].isdigit():
            curnum=(curnum*10)+int(expression[i])
        else:
            queue.append(curnum)
            curnum=0
            if signs:
                if preceds[expression[i]]<preceds[signs[-1]]:
                    queue.append(signs.pop())
                    
            signs.append(expression[i])

    queue.append(curnum)
    queue.extend(signs[::-1])
    res=0
    arr=[]

    for i,val in enumerate(queue):

        if str(val) not in "-+^*":
            arr.append(val)
        else:
            val1=arr.pop()
            val2=arr.pop()
            if val=="-":res=(val2-val1)
            elif val=="+": res=(val1+val2)
            elif val=="*": res=(val1*val2)
            else: res=(val2^val1)
            arr.append(res)

    return arr[0]


print(calculate("4*3+2^2^2"))   
print(calculate("23^2"))   







