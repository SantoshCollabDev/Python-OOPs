'''
Polymorphism:
A single entity/function serving different needs based on the input

Ex: len() function
'''
# This is an example of Polymorphism
# where the single function len() does know how to handle different kinds of objects as expected

name = 'Santosh'
print(len(name))      # Returns LENGTH OF THE STRING

some_list = ["Some","name"]
print(len(some_list))   # Returns LENGTH OF THE LIST