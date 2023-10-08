class Roi:
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.total_invest = 0
        self.inflow = 0
        self.value = 0

    def add_income(self, income):
        if income >= 0:
            self.income += income
            print(self.income)

    def add_expense(self, expenses):
        if expenses >= 0:
            self.expenses += expenses
            print(self.expenses)

    def cash_flow(self):
        if self.income and self.expenses >= 0:
            inflow = (self.income - self.expenses) * 24
            print(inflow)
            return inflow
        else:
            return 0

    def prop_value(self, prop_val):
        self.value += prop_val
        self.total_invest += (self.value * 0.2)
        print(self.value * 0.2)

    def misc_costs(self, misc):
        print(f'self.total_invest += {misc}')
        self.total_invest += misc

    def calculate_roi(self):
        print(f'{self.inflow / self.total_invest * 100}')

        roi_done = (self.inflow / self.total_invest) * 100
        print(roi_done)
        return roi_done

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
