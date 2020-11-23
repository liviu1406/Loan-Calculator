# put your python code here

import math

first_input = float(input())
second_input = float(input())
operation = input()


if second_input == 0.0 and operation in ["mod", "div", "/"]:
    print("Division by 0!")
elif operation == '+':
    print(first_input + second_input)
elif operation == '-':
    print(first_input - second_input)
elif operation == '/':
    print(first_input / second_input)
elif operation == '*':
    print(first_input * second_input)
elif operation == 'mod':
    print(first_input % second_input)
elif operation == 'pow':
    print(first_input ** second_input)
elif operation == 'div':
    print(int(first_input) // int(second_input))

