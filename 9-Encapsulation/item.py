import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        # Since we have defined name as a read-only attribute using @property decorator
        # prefix underscore(__) to the name attribute to allow assignment;
        # __variable: makes variable private which can be only accessed from respective class
        self.__name = name
        self.__price = price     # Change price to PRIVATE
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        # print("You are trying to get name")
        return self.__name   # prefix name with underscore(__) as did above

    @name.setter
    # setter --- allows setting values of read only variables
    def name(self, newval):
        print("You are trying to set name")
        if len(newval) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = newval

    @property
    def price(self):
        return self.__price

    def apply_increment(self, increment_prcnt):
        self.__price = self.__price + self.__price * increment_prcnt

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

