#using *args
def add(*args):
    sum = 0
    for each in args:
        sum += each
    return sum

def subtract(*args):
    difference = 0
    for each in args:
        difference -= each
    return difference

def multiply(*args):
    multiply= 0
    for each in args:
        multiply *= each
    return multiply

def divide(a,b):
    if b ==0:
        return "Error division by 0"
    return a / b

print(add(5,6))