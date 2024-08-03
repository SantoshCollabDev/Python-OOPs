''' Class Attributes Vs Instance/Object Attribute:
Attributes that belong to class and accessible to all instances of the class.
Note: When a class attribute is referred by a object/instance of class -
first object attributes are checked in constructor if not found then it refers
to the class attribute '''

class Item:
    # CLASS ATTRIBUTE - pay_rate
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
      # Validate the arguments before setting object attributes
      assert price >= 0, f"Price {price} is not greater or equal to Zero!"
      assert quantity >= 0, f"Quantity {quantity} is not greater or equal to Zero!" 

      # Set Object Attributes 
      self.name = name
      self.price = price
      self.quantity = quantity

      # Add/append each instance defined to list ---> all[]
      Item.all.append(self)

    def __repr__(self):  # formats the output in a string format
       return f"Item('{self.name}', {self.price}, {self.quantity})"

    def calculate_total_price(self):
      return self.price * self.quantity
    
    def apply_discount(self):
       self.price = self.price * self.pay_rate  # access pay_rate using SELF --- PREFERRED METHOD

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# for instance in Item.all:
#    print(instance.name)

print(Item.all) # NOT Readable output  --- USE __repr__()


