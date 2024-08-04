'''
Polymorphism:
A single entity/function serving different needs based on the input

'''
from phone import Phone    # Phone is a Child class of Item class
from keyboard import Keyboard

item1 = Keyboard("Mech.Keyboard", 500, 3)   # defining an instance of child

# Here the apply_discount function works same as it would have worked for phone instances
item1.apply_discount()

print(item1.price)
