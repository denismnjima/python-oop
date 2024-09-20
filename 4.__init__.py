# In the previous example you have to have hardcode properties everytime you create an instance of a class.
'''
item1 = Item()
item1.name = 'Phone'
item1.price = 15000
item1.quantity = 5
'''
from six import print_


# you can use __init__, which is one of the  magic/dunder/special  methods in python.
# The method is run automatically when a class instance is created
#The quantity is set to 0 making it a non-mandatory parameter

class Item:
    def __init__(self,name,price,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item('phone',15000)
total = item1.calculate_total_price()
print(total)