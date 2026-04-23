# Net Salary Calculator

gross_salary = float(input('Enter your Gross monthly salary: '))

print('\nChoose your personal income tax:')
print('20%')
print('25%')
print('32%')

tax = float(input('Enter your tax %: '))

# Validate tax input
if tax == 20 or tax == 25 or tax == 32:

    pension = input('Do you participate in pension program? (yes/no): ')

    social_security = 19.5  # fixed
    pension_rate = 3        # %

    # Base tax calculation
    total_tax = tax + social_security

    # Add pension if applicable
    if pension.lower() == 'yes':
        total_tax = total_tax + pension_rate

    # Final salary calculation
    tax_amount = gross_salary * (total_tax / 100)
    final_salary = gross_salary - tax_amount

    print('Your salary after tax is:', round(final_salary, 2))

else:
    print('Please choose correct personal income tax')