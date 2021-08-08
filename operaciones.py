def suma(x,y):
    return x + y

def rest(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    if y == 0:
        return "Division entre 0"
    else:
        return x / y

def mayor3(x,y,z):
    r = x
    if r < y:
        r = y
    if r < z:
        r = z
    return r