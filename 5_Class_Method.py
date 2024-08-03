import csv

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            # use a method to directly read csv
            reader = csv.DictReader(f)
            items = list(reader)

        # instantiate the instances
        for item in items:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )

    def apply_discount(self):
        self.price = self.price * self.pay_rate  # access pay_rate using SELF --- PREFERRED METHOD

Item.instantiate_from_csv()
print(Item.all)