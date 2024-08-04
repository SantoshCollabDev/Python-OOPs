# 4 key principles of OOPS
'''
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

Encapsulation:
Encapsulation allows you to define controlled access to data stored inside objects of your class.
This allows you to write clean, readable, and efficient code and prevent accidental changes or
deletion of your class data.
'''
from item import Item

# Control the access and update of the price through encapsulation
# 1. make it private
# 2. define getter & setter methods

item1 = Item("MyItem", 750)

# price attribute is controlled through the class methods
item1.apply_increment(0.2)
print(item1.price)

item1.apply_discount()
print(item1.price)




