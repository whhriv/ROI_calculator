# from models import Location
# from properties import Properties

class Properties:
    def __init__(self):
        self.cashout = []
        self.cashin = []
        self.prop_id = []
                    #  Create a new property with new_prop variable
    def create_property(self):
        property_name = input('What property do you want to calculate?  ')
        if property_name in [i.property_name for i in self.prop_id]:
            print(f"The property: {property_name} already exists")
        else:
            new_prop = Location(property_name)
            #add new property to look at with property_name input
            self.prop_id.append(new_prop)
            print(f"{new_prop} has been created")
    def init_invest(self, cashout):
        cost_close 


