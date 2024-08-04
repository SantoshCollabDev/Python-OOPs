# When to use class methods and when to use static methods?
class Item:
    @staticmethod
    def is_interger():
        '''
        This should do something that has a relationship with the class,
        but not something that must be unique per instance!
        '''
    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do something that has a relationship with the class,
        but usually, those are used to manipulate different structures of data
        to instantiate objects, like we have done with CSV.
        '''

# STATIC methods doesn't pass the object reference as 1st argument

# CLASS methods passes the CLASS (not object ex: self ) reference as 1st argument


