'''
Inheritance:
Mechanism that allows to RE-USE the code across all classes

Ex: Phone is a child class of an item (parent) and where it(child) represents a kind of item

Inheritance allows us define more classes while re-using the existing class methods/attributes
and letting us code any specific additional sttributes and/or methods in the new(child) classes
'''
from phone import Phone    # Phone is a Child class of Item class

item1 = Phone("MotoG5HV1", 1000, 3)   # defining an instance of child

item1.apply_increment(0.2)     # child instance can access the parent method as it inherits it
print(item1.price)





