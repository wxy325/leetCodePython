
def evalRPN(tokens):
    if not len(tokens):
        return 0

    temp = []
    opDict = {'+':lambda a,b:a+b,
              '-':lambda a,b:a-b,
              '*':lambda a,b:a*b,
              '/':lambda a,b:int(float(a)/b),}  #除法小数直接取整

    for a in tokens:
        try:
            op = opDict[a]
            r = temp.pop()
            l = temp.pop()
            v = op(l,r)
            temp.append(v)
        except KeyError:
            a = int(a)
            temp.append(a)

    return temp[0]

if __name__ == '__main__':
    l = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(l))

