def add(a,b):
    return a + b

def subtract(a,b):
    return a -b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b ==0:
        return "Error division by 0"
    return a / b

def get_user_input():
    operation = input("Enter operation (+, -, /, *)")
    if operation not in['+', '-', '/', '*']:
        print("Invalid operation")
        return None, None, None

    a = float(input("Enter your fist number:  "))
    b = float(input("Enter your second number:  "))

    return operation, a, b 

def main():
    while True:
        operation, num1, num2, = get_user_input()
        result = 0
        if operation is None:
            return 0 
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1,num2)
        elif operation == '/':
            result = divide(num1,num2)
        else:
            result = multiply(num1,num2)

        print(f"The reslut is: {result}")
        
        next_calculation = input("Do you want to prtform another calculation:? (Yes_No)':")
        if next_calculation.lower() != "yes":
            break 
                                 
main()

 