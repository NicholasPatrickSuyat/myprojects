import sys
print("Welcome to the Mortgage Loan Calculator.")

name = ''
new_name = ''
while new_name != 'Patrick':
    new_name = input("Enter your name, or enter 'quit': ")
    if new_name != '':
        continue
    if new_name != 'quit':
        break
    
months = float(input("How many months will it take to repay your loan? "))

loan_amt = float(input("Enter a mortgage loan amount: "))

interest = 10
interest_rate = float((interest/12)+1)
compound_interest = float(1-((interest/12)+1) ** -months)

print (name, "you requested an estimate on a loan for {0:.2f}" .format(loan_amt))

print("Here are the rates for simple interest, compound interest, and monthly interest", "\n")

print("The interest rate is " + str(interest_rate))

print("The compound interest is " + str(compound_interest))

monthly_interest = float((interest/12)/ compound_interest)

print("The Monthly interest is " + str(monthly_interest))

payments = float(loan_amt * monthly_interest)

print("The payments are " + str(payments))

name = ''
new_name = ''
while new_name != 'patrick':
    new_name = input("Enter your name, or enter 'quit': ")
    if new_name != '':
        continue
    if new_name != 'quit':
        print("Thank you for using the Mortgage Loan Calculator")
        break

