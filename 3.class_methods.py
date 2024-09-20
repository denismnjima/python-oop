# methods are functions made inside methods

class Item:
    def calculate_total_price(self,x,y):
        return  x * y


# by default class methods receive a positional parameter, thus you must provide at least one
# parameter when creating a method. By convention it is assigned to the self keyword.

item1 = Item()
item1.name = 'Phone'
item1.price = 15000
item1.quantity = 5
print(item1.calculate_total_price(item1.price,item1.quantity))