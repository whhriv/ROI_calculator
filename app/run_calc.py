# BLOG
# from msilib.schema import SelfReg
from models import Properties
from typing import Self
from models import Properties
prop = Properties()
def calc_roi(self):
    while True:
        # quit = input('quit')
        # if quit == 'quit':
        #     break
        # else:
        #     continue
        
        cost_close = input('How much did you close on the property? ') 
        if cost_close:
            prop.propval.append(cost_close)
            down_payment = 0.2 * int(cost_close)
            print(f"for a ${cost_close} property at 20% you have a {down_payment} down payment")
            prop.investment.append(down_payment)
            print("We are going to add 3k and 7k for closing and rehab costs, respectively")
            misc = 10000
            prop.investment.append(misc)
        prop_tax = input('How much are taxes on this property?')
        if prop_tax:
            prop.cashout.append(prop_tax)
        prop_insur = input('How much is insurance on this property?')
        if prop_insur:
            prop.cashout.append(prop_insur)
        prop_mort = input('What is the monthly mortgage payment? ')
        if prop_mort:
            prop.cashout.append(prop_mort)
        prop_util = input('total cost of utilities (gas, electric, etc): ')
        if prop_util:
            prop.cashout.append(prop_util)
        prop_manage = input('How much does it cost for property management? ')
        if prop_manage:
            prop.cashout.append(prop_manage)
        rent = input('how much to charge for rent per month?  ')
        if rent:
            prop.cashin.append(rent)

        monthly_costs = sum(map(int, prop.cashout))
        annual_rent = int(rent) * 12
        annual_costs = monthly_costs*12
        invest_int = sum(map(int, prop.investment))
        profit = annual_rent - annual_costs
        print(f'profit: {profit}')
        print(f'annual costs: {annual_costs}')
        prop.annual.append(annual_costs)  
        if monthly_costs != 0:
            CoCROI = (profit / invest_int) * 100
            # prop.returnroi = (annual_rent / annual_costs)*100
            print(f' return on roi % {CoCROI}')
        # return prop.returnroi
        # print(prop.cashout)
        # print(prop.cashin)
        # print(prop.returnroi)
        print(f"Cash-on-Cash Return on Investment: {CoCROI}%")


#####---------------TEST CODE----------------###########
        # moneyspent = sum(map(int, prop.cashout))
        # totalinvestment = int(down_payment) + 3000 + 7000
        # print(f'total investment: {totalinvestment}')
        # annual_rent = int(2000 * 12)
        # print(f'annual rent {annual_rent}')
        # print(f'cash out expenses: {moneyspent}')
        # annual_cashflow = annual_rent - moneyspent
        # print(f'annual cashflow: {annual_cashflow}')
        # cash_on_roi =  int(annual_cashflow)  /  int(totalinvestment)
        # print(f' cash on roi:  {cash_on_roi}')
        # percentage = cash_on_roi * 100
        # print(f'percentage: {percentage}')
#####---------------TEST CODE----------------###########

# Print the calculated ROI
        return prop.returnroi

print(prop.cashout)
print(prop.cashin)
print(prop.returnroi)
print(f"Cash-on-Cash Return on Investment: {prop.returnroi}%")
  


if __name__ == "__main__":
    calc_roi(Self)

