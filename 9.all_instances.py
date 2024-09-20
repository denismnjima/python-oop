
class Item:
    all = []
    def __init__(self,name:str,price:float,quantity:int=0):
        assert  price>=0, f"price: {price} should be greater than or equal to zero"
        assert  quantity>=0, f"quantity: {quantity} should be greater than or equal to zero"
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.quantity

# if I enter a string in prices place, I get a warning marker
item1 = Item('phone',15000,5)
item2 = Item('laptop',45,5)
item3 = Item('earbuds',678,5)
item4 = Item('mouse',67,5)

for item_name in Item.all:
    print(item_name.name)