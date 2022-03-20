#define function 

def calculate():
    operation = input('''Choose the operator for perfoming operation
    + Addition
    - Subtraction
    * Multiplication
    / Division \n''')

    number_1 = int(input("> Enter the first number! \n"))
    number_2 = int(input("> Enter the second number! \n"))

    if operation == '+':
        result = number_1 + number_2

    elif operation == '-':
        result = number_1 - number_2

    elif operation == '*':
        result = number_1 * number_2

    elif operation == '/':
        result = number_1 / number_2

    else:
        result = "You have not entered a valid operator, choose a valid operator!"


    print("> The answer is " + str(result))

#call function 
calculate()
