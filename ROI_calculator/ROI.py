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
            return self.income
    def add_expense(self, expenses):
        if expenses >= 0:
            self.expenses += expenses
            print(self.expenses)
            return self.expenses
    
    ##PROBLEMATIC
    def cash_flow(self, income, expenses):
        # if self.income:
        incomeX = (self.income - self.expenses) 
        self.inflow = incomeX * 12
        print(self.inflow)
        return self.inflow
        # else:
        #     return 0

    def prop_value(self, prop_val):
        self.value += (prop_val * 0.2)
        # self.total_invest += (self.value * 0.2)
        print(f"{self.value}")
        return self.value
    
    def misc_costs(self, misc):
        print(f'{self.total_invest} + {misc}')
        self.total_invest += misc
        return self.total_invest

    def calculate_roi(self):
       
        roi_done = (self.inflow / self.total_invest) * 100
        print(f' roi: {roi_done}')
        return (self.inflow / self.total_invest) * 100
    
# print('{self.income}')
# print('{income}')
# print("""         
# Total Income: {income}
# Total Expenses: {expenses}
# Total investment: {total_invest} 
# {inflow}
# {roi_done} """)