''' Class Attributes Vs Instance/Object Attribute:
Attributes that belong to class and accessible to all instances of the class.
Note: When a class attribute is referred by a object/instance of class -
first object attributes are checked in constructor if not found then it refers
to the class attribute '''

class Item:
    # CLASS ATTRIBUTE - pay_rate
    pay_rate = 0.8  # The pay rate after 20% discount
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
    
    def apply_discount(self):
       # payrate can not be accssed directly. use clas or object
      #  self.price = self.price * Item.pay_rate  # access pay_rate using class
      #  self.price = self.price * item1.pay_rate  # access pay_rate using object
       self.price = self.price * self.pay_rate  # access pay_rate using SELF --- PREFERRED METHOD

    
item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# ****************************************************
# class variable accessed through its instances 
# ****************************************************
# print(Item.pay_rate)   # Access class attribute USING CLASS NAME
# print(item1.pay_rate)  # since pay_rate is not found at item1. it pulls it from class
# print(item2.pay_rate)

# ****************************************************
# to know ALL the attributes of a class or object ----->  MAGIC METHOD:  __dict__
# Note: __dict__ : takes all attributes and converts them to dictionary hence the keyword __dict__
# ****************************************************
# print(Item.__dict__)
# print("")
# print(item1.__dict__)

item1.apply_discount()
item2.apply_discount()

print(item1.price)
print(item2.price)

# CASE: for item3 we want to have a different discount rate - say 30%
# then assign the class varaible directly to the object as below
item3 = Item("Keyboard", 300, 1)
item3.pay_rate = 0.7  # defining 30% discount
item3.apply_discount()
print(item3.price)
