# what if we wanted to control the data-type of parameters. We can use typings

class Item:
    def __init__(self,name:str,price:float,quantity:int=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity

# if I enter a string in prices place, I get a warning marker
item1 = Item('phone','15000',5)
total = item1.calculate_total_price()
print(total)