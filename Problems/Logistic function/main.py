import math

user_input = int(input())

formula = 1 / ( 1 + math.exp(-user_input))

print(round(formula, 2))

# 1 / (1 + math.exp(-x)) is ho