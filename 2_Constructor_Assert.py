'''
__init__ : constructor gets called upon instance creation

double underscore methods ---> magic/dunder methods

self --> default argument always passed on calling a class method

set default values for non-mandatory/optional arguments i.e. for which values 
may not be always known 
Example: quantity set to default value as below...
         def __init__(self, name: str, price: float, quantity=0):

To avoid type issues always specify the type of values expected for 
each of the arguments
Example: name as string, price as float etc as shown below...
         def __init__(self, name: str, price: float, quantity=0):


'''


class Item:
  def __init__(self, name: str, price: float, quantity=0):

    # Validate the arguments before setting object attributes
    assert price >= 0, f"Price {price} is not greater or equal to Zero!"
    assert quantity >= 0, f"Quantity {quantity} is not greater or equal to Zero!" 

    # Set Object Attributes 
    self.name = name
    self.price = price
    self.quantity = quantity
  
  def calculate_total_price(self):
    return self.price * self.quantity
    
item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
