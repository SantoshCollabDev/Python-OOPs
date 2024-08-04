# different DECORATORS helps us CONTROL THE LEVEL OF ACCESS to the class attributes

from item import Item
from phone import Phone


item1 = Item("MyItem", 750)
# in class name is prefixed with underscore but while accessing through objects/instnces
# it is referred w/o any prefix

# name is read only variable so its value cant be changed with re-assignment
# item1.name = "OtherItem"   # changing/new-assignment not allowed

# change the readonly variable value using setter @name.setter
item1.name = "OtherItemLong"
print(item1.name)



