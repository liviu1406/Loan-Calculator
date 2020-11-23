import math
import argparse


loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# parser = argparse.ArgumentParser(description='Credit calculator')
# parser.add_argument('--type', type=str, help='select between annuity or diff')
# parser.add_argument('--principal', type=int, help='input principal amount')
# parser.add_argument('--interest', type=float, help='input loan interest')
# parser.add_argument('--payment', type=float, help='input monthly payment')
# parser.add_argument('--periods', type=int, help='input number of periods')
# args = parser.parse_args()


def months_to_years(months):
    years = 0
    if months < 12 and years == 0:
        return f"{months} months"
    else:
        while months >= 12:
            months -= 12
            years += 1
            if months == 12:
                months -= 12
                years += 1
                return f"It will take {years} years to repay this loan!"
            else:
                return f"It will take {years} years and {months} months to repay this loan!"


def n_monthly_payments():
    loan_principal = int(input("Enter the loan principal:\n"))
    monthly_payment = float(input("Enter the monthly payment:\n"))
    loan_interest = float(input("Enter the loan interest:\n")) / 1200
    months = math.log((monthly_payment / (monthly_payment - (loan_interest * loan_principal))), 1 + loan_interest)
    exact_months = math.ceil(months)
    # print(exact_months)
    total = 0
    for m in range(1, exact_months + 1):
        total += math.ceil(monthly_payment)
    overpayment = total - loan_principal
    return months_to_years(exact_months) + f"\nOverpayment = {math.ceil(overpayment)}"


def monthly_payment():
    loan_principal = int(input("Enter the loan principal:\n"))
    months = int(input("Enter the number of periods:\n"))
    loan_interest = float(input("Enter the loan interest:\n")) / 1200
    monthly_payment = loan_principal * ((loan_interest * ((1 + loan_interest)**months)) / (((1 + loan_interest)**months)-1))
    total = 0
    for m in range(1, months + 1):
        total += math.ceil(monthly_payment)
    overpayment = total - loan_principal
    return f"Your monthly payment = {math.ceil(monthly_payment)}!\n" \
           f"Overpayment = {math.ceil(overpayment)}"


def loan_principal():
    monthly_payment = float(input("Enter the annuity payment:\n"))
    months = int(input("Enter the number of periods:\n"))
    loan_interest = float(input("Enter the loan interest:\n")) / 1200
    loan_principal = monthly_payment / ((loan_interest * ((1 + loan_interest)**months)) / (((1 + loan_interest)**months) - 1))
    total = 0
    for m in range(1, months + 1):
        total += math.ceil(monthly_payment)
    overpayment = total - loan_principal
    return f"Your loan principal = {math.floor(loan_principal)}!\n\n" \
           f"Overpayment = {math.ceil(overpayment)}"


def differentiated_payment():
    loan_principal = int(input("Enter the loan principal:\n"))
    number_of_payments = int(input("Enter the number of payments:\n"))
    loan_interest = float(input("Enter the loan interest:\n")) / 1200
    total = 0
    for m in range(1, number_of_payments + 1):
        diff_payment = loan_principal / number_of_payments + loan_interest \
                       * (loan_principal - (loan_principal * (m - 1)) / number_of_payments)
        total += math.ceil(diff_payment)
        print(f"Month {m}: payment is {math.ceil(diff_payment)}")
    overpayment = total - loan_principal
    return f'\nOverpayment = {overpayment}'


print('What do you want to calculate?\ntype "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
choice = input('type "d" for differentiate payment:\n')


if choice == "n":
    print(n_monthly_payments())
elif choice == "a":
    print(monthly_payment())
elif choice == "p":
    print(loan_principal())
elif choice == "d":
    print(differentiated_payment())


