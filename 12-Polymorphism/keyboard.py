from item import Item

class Keyboard(Item):
    pay_rate = 0.7    # common discount rate for all keyboards
    def __init__(self, name: str, price: float, quantity=0):
        # Call to super function to have access to all attributes / methods of parent class
        super().__init__(
            name, price, quantity
        )