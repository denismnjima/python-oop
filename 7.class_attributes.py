# Instance attributes are attributes created at instance level
# Example: In the example below name,price and quantity are instance attributes.
# They can be accessed from an instance only Eg. item.name -> Remember item1 is an instance of Item


class Item:
    pay_rate = 0.8
    def __init__(self,name:str,price:float,quantity:int=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item('phone',15000,5)
#pay_rate is a class attribute. It can be accessed without an instance

print(Item.pay_rate)

# It can also be accessed at instance level.
print(item1.pay_rate)
item1.apply_discount()
