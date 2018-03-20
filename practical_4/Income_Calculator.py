"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    last_month = int(input("How many months? "))

    for month in range(1, last_month + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)
    report_income(incomes, last_month)


def report_income(incomes, current_month):
    total = 0
    print("\nIncome Report\n-------------")
    for month in range(1, current_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
