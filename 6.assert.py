# Typings are good for telling the programmer what is expected.
# However, they do not serve as validation
# You can use the assert keyword to validate. Assert has the following syntax:
# assert condition, message
# Running the code below will output an assertion error

class Item:
    def __init__(self,name:str,price:float,quantity:int=0):
        assert  price>=0, f"price: {price} should be greater than or equal to zero"
        assert  quantity>=0, f"quantity: {quantity} should be greater than or equal to zero"
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity

# if I enter a string in prices place, I get a warning marker
item1 = Item('phone',-15000,5)
total = item1.calculate_total_price()
print(total)