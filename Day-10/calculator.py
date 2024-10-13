from arts import logo
import os

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    num1 = int(input("What's your first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:        
        operation_symole = input("Pick an operation: ") 
        num2 = int(input("What's your next number: "))
        calcutation_function = operations[operation_symole]
        answer = calcutation_function(num1, num2)

        print(f"{num1} {operation_symole} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: \n") == "y":
            num1 = answer
        else:
            clear_console()
            calculator()   

calculator()    
    

    
        

   
