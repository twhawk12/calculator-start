from art import logo


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    calculation = True 
    
    while calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        proceed = input(f"Type 'y' to continue calculatiing with {answer}, or type 'n' to start a new: ")
        if proceed == "y":
            num1 = answer
        else:
            calculation = False 
            calculator()



calculator()