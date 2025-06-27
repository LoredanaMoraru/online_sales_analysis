class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Produs: {self.name}")
        print(f"Preț: {self.price} RON")
        print(f"Stoc disponibil: {self.quantity}")

    def update_quantity(self, amount):
        self.quantity += amount
        print(f"Stocul actualizat pentru {self.name}: {self.quantity}")
