"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Loop until break
while True:ii
    # get user input
    user_input = input("Enter your equation: > ")
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
    

    if ""
    # if statement for each operation 
        # calls matching function for operation using other tokens
    

    
    
