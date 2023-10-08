# from properties import Properties
from random import randint

class Properties:

    def __init__(self):
        # self.data = data if data is not None else {}
        self.cashout = []
        self.propval = []
        self.cashin = []
        self.annual = []
        self.returnroi = []
        self.investment = []
        
    def __str__(self):
        return f"""
        {self.out} """
        
    def __repr__(self):
        return f"||| {self.income} - {self.expenses} = {self.returnroi}% |||"



class Roi:
    def __init__(self, cash_out, cash_in):
        pass

    def __str__(self):
        pass
    def __repr__(self):
        pass

