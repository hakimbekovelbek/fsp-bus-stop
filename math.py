def abs(x):
    if x >= 0: return x
    else: return -x

def factorial(x):
    if x == 1: return 1
    return factorial(x - 1) * x