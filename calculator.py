"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Loop until break
while True:
    # get user input
    user_input = input("Enter your equation: ")
    # tokenize input
    tokens = user_input.split(" ")

    # if first token is q then quit
    if "q" in tokens:
        print("Thank you, Bye")
        break 

    # assign variable names to tokens
    operation = tokens[0]
    num1 = tokens[1]

    if len(tokens) < 3:
        num2 = "0"

    else:
        num2 = tokens[2]

    if len(tokens) > 3:
        num3 = tokens[3]

    # variable assignment for result of function
    answer = None


    # if statement for each operation 
    if operation == "+":
    # calls function that matches operation 
    # using the float other tokens as numbers
        answer = add(float(num1), float(num2))

    elif operation == "-":
        answer = subtract(float(num1), float(num2))

    elif operation == "*":
        answer = multiply(float(num1), float(num2))

    elif operation == "/":
        answer = divide(float(num1), float(num2))

    elif operation == "square":
        answer = square(float(num1))

    elif operation == "cube":
        asnwer = cube(float(num1))

    elif operation == "pow":
        answer = power(float(num1), float(num2))

    elif operation == "mod":
        answer = mod(float(num1), float(num2))

    else: 
        answer = "Please enter an operator followed by 2 integers"

    print(answer)

    
