class MenuItem:
    """Base class for menu items."""

    def __init__(self, name: str, price: float):
        """Initialize a MenuItem object with name and price parameters.

        - param name: Name of the MenuItem object.
        - param price: Price of the MenuItem object.
        """
        self._name = name
        self._price = price

    def get_name(self):
        """Return the name of the MenuItem object."""
        return self._name

    def set_name(self, name: str):
        """Set the name of the MenuItem object.

        - param name: New name to set.
        """
        self._name = name

    def get_price(self):
        """Return the price of the MenuItem object."""
        return self._price

    def set_price(self, price: float):
        """Set the price of the MenuItem object.

        - param price: New price to set.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = price

    def total_price(self, quantity: int = 1) -> float:
        """Calculate the total price based on quantity.

        - param quantity: Quantity of the MenuItem.
        - return: Total price as a float.
        """
        return self._price * quantity

    def __str__(self):
        """Return a string representation of the MenuItem object."""
        return f"{self._name} - ${self._price:.2f}"


class Beverage(MenuItem):
    """Beverage class inherits methods and attributes from MenuItem class."""

    def __init__(self, name: str, price: float, size: str):
        """Initialize a Beverage object with name, price, and size parameters.

        - param name: Name of the Beverage object.
        - param price: Price of the Beverage object.
        - param size: Size of the Beverage object (e.g., Small, Medium, Large).
        """
        super().__init__(name, price)
        self._size = size

    def get_size(self):
        """Return the size of the Beverage object."""
        return self._size

    def set_size(self, size: str):
        """Set the size of the Beverage object.

        - param size: New size to set.
        """
        self._size = size

    def __str__(self):
        """Return a string representation of the Beverage object."""
        return f"{self._name} - ${self._price:.2f} ({self._size})"


class Appetizer(MenuItem):
    """Appetizer class inherits methods and attributes from MenuItem class."""

    def __init__(self, name: str, price: float, portion_size: str):
        """Initialize an Appetizer object with name, price, and portion size.

        - param name: Name of the Appetizer object.
        - param price: Price of the Appetizer object.
        - param portion_size: Portion size of the Appetizer object (e.g., 6 pieces, 1 plate).
        """
        super().__init__(name, price)
        self._portion_size = portion_size

    def get_portion_size(self):
        """Return the portion size of the Appetizer object."""
        return self._portion_size

    def set_portion_size(self, portion_size: str):
        """Set the portion size of the Appetizer object.

        - param portion_size: New portion size to set.
        """
        self._portion_size = portion_size

    def __str__(self):
        """Return a string representation of the Appetizer object."""
        return f"{self._name} - ${self._price:.2f} ({self._portion_size})"


class Maincourse(MenuItem):
    """Maincourse class inherits methods and attributes from MenuItem class."""

    def __init__(self, name: str, price: float):
        """Initialize a Maincourse object with name and price parameters.

        - param name: Name of the Maincourse object.
        - param price: Price of the Maincourse object.
        """
        super().__init__(name, price)

    def __str__(self):
        """Return a string representation of the Maincourse object."""
        return f"{self._name} - ${self._price:.2f}"


class Order:
    """Order class is used to create and calculate the bill."""

    def __init__(self):
        """Initialize an Order with an empty list of items."""
        self._order_items = []

    def add_menu_item(self, item: MenuItem, quantity: int = 1):
        """Add a MenuItem object to the order.

        - param item: A MenuItem instance to be added.
        - param quantity: Quantity of the MenuItem to add.
        """
        self._order_items.append((item, quantity))

    def calculate_total_price(self) -> float:
        """Calculate the total bill with an optional discount for beverages.

        - return: Total price as a float.
        """
        total = 0
        has_maincourse = any(isinstance(item, Maincourse) for item, _ in self._order_items)

        for item, quantity in self._order_items:
            if has_maincourse and isinstance(item, Beverage):
                total += item.total_price(quantity) * 0.9  # 10% discount on beverages
            else:
                total += item.total_price(quantity)

        return total

    def __str__(self):
        """Return a string representation of the Order object."""
        return "\n".join(
            f"{quantity}x {item}" for item, quantity in self._order_items
        )


class Payment:
    """Base class for different payment methods."""

    def pay(self, amount: float):
        """Abstract method to process payment.

        - param amount: The amount to be paid.
        """
        raise NotImplementedError("Subclasses must implement the pay() method.")


class CardPayment(Payment):
    """Class for card payment method."""

    def __init__(self, card_number: str, cvv: int):
        """Initialize a CardPayment object.

        - param card_number: Card number for the payment.
        - param cvv: CVV code of the card.
        """
        self._card_number = card_number
        self._cvv = cvv

    def pay(self, amount: float):
        """Process the payment using a card.

        - param amount: The amount to be paid.
        """
        print(f"Paying ${amount:.2f} with card ending in {self._card_number[-4:]}")


class CashPayment(Payment):
    """Class for cash payment method."""

    def __init__(self, cash_given: float):
        """Initialize a CashPayment object.

        - param cash_given: The cash amount provided for payment.
        """
        self._cash_given = cash_given

    def pay(self, amount: float):
        """Process the payment using cash.

        - param amount: The amount to be paid.
        """
        if self._cash_given >= amount:
            change = self._cash_given - amount
            print(f"Paid ${amount:.2f} in cash. Change: ${change:.2f}")
        else:
            print(f"Insufficient funds. Need ${amount - self._cash_given:.2f} more.")


# Example Usage
menu = [
    Beverage("Coke", 2.5, "Large"),
    Appetizer("Spring Rolls", 5.0, "Medium"),
    Maincourse("Spaghetti", 12.0),
    Beverage("Fanta", 2.5, "Small"),
]

order = Order()
order.add_menu_item(menu[0], 2)  # 2 Cokes
order.add_menu_item(menu[1], 1)  # 1 Spring Rolls
order.add_menu_item(menu[2], 1)  # 1 Spaghetti

print("Order:")
print(order)
print(f"Total Price: ${order.calculate_total_price():.2f}")

payment_method = CardPayment("1234567890123456", 123)
payment_method.pay(order.calculate_total_price())