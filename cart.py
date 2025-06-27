# cart.py

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"{product.name} a fost adăugat în coș.")

    def display_cart(self):
        if not self.cart_items:
            print("Coșul este gol.")
        else:
            print("\n=== Conținutul coșului ===")
            for item in self.cart_items:
                item.display_info()
                print("-" * 30)

    def calculate_total(self):
        total = sum(p.price * p.quantity for p in self.cart_items)
        print(f"Total de plată: {total} RON")
        return total
