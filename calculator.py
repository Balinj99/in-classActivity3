def add(a, b):
    return a + b

def sub(a, b):
    return a-b

def mult(a, b):
    return a * b

def div(a, b):
    if(b == 0):
        print("Error. You can not divide by 0")
        return 0
    else:
        return a / b
