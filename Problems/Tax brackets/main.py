import math

income = int(input())


def mycalc():
    tax = percent * 0.01
    # print(tax)
    calculated_tax = income * tax
    # print(calculated_tax)
    print(f'The tax for {income} is {percent}%. That is {int(round(calculated_tax))} dollars!')


if 0 <= income <= 15527:
    percent = 0
    mycalc()
elif 15528 <= income <= 42707:
    percent = 15
    mycalc()
elif 42708 <= income <= 132406:
    percent = 25
    mycalc()
elif 132407 <= income:
    percent = 28
    mycalc()




