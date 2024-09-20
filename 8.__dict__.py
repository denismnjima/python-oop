#The magic property __dict__ is used lo list class or instance properties
class Item:
    pay_rate = 0.8
    def __init__(self,name:str,price:float,quantity:int=0):
        self.name = name
        self.price = price
        self.quantity = quantity

item1 = Item('phone',15000,5)

print(Item.__dict__)

print(item1.__dict__)