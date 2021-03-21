from art import logo

  

#add
def add(n1,n2):
    return n1+n2

#subtract
def subtract(n1,n2):
    return n1-n2

#multiply
def multiply(n1,n2):
    return n1*n2

#divide
def divide(n1,n2):
    return n1/n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}





def calculator():
    print(logo)
    num1 = float(input("what is the first number?: ").strip())

    continue_calculating = True

    while continue_calculating:

        for symbol in operations:
            print(symbol)

        operation_symbol = input('Pick an operation from the line above?: ').strip()

        num2 = float(input("what is the second number?: ").strip())

        compute = operations[operation_symbol]
        num3 = compute(num1,num2)

        print(f'{num1} {operation_symbol} {num2} = {num3}')

            
        if input(f"Type 'y' to continue calculating with {num3}, or type 'n' to perform a new calculation: ") == 'y':
            num1 = num3
        else:
            continue_calculating == False
            calculator()

calculator()



