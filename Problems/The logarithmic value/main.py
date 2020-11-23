import math

first_input = abs(int(input()))
second_input = int(input())

if second_input <= 1:
    form = math.log(first_input)
    print(round(form, 2))
else:
    form = math.log(first_input, second_input)
    print(round(form, 2))

