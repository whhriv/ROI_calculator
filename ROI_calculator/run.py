from ROI import Roi
def run_stuff():
    roi = Roi()
    while True:
        try:
            prop_val = int(input("For Down Payment @ 20% /enter closing cost: "))
            roi.prop_value(prop_val)
        except ValueError:
            print("Please enter a valid number")

        try:
            misc = int(input("Other costs put into property, i.e., rehab, roof, repairs: "))
            roi.misc_costs(misc)
        except ValueError:
            print("Please enter a valid number")

        try:
            rent = int(input('How much for rent? '))
            roi.add_income(rent)
        except ValueError:
            print("Please enter a valid number for rent")

        try:
            utilities = int(input('How much Utilities? (laundry, storage, misc): '))
            roi.add_income(utilities)
        except ValueError:
            print("Please enter a valid number")

        try:
            tax = int(input('How much did you pay for taxes? '))
            roi.add_expense(tax)
        except ValueError:
            print("Please enter a valid number")

        try:
            insurance = int(input('How much for Insurance? '))
            roi.add_expense(insurance)
        except ValueError:
            print("Please enter a valid number for rent")

        try:
            mortgage = int(input('How much is the mortgage? '))
            roi.add_expense(mortgage)
        except ValueError:
            print("Please enter a valid number")

        roi.calculate_roi()

        print(f"""
        Total Income: {roi.income}
        Total Expenses: {roi.expenses}
        Total investment: {roi.total_invest} 
        Inflow: {roi.inflow}
        ROI: {roi.calculate_roi()}%
        """)


if __name__ == "__main__":
    run_stuff()