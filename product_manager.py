from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Adăugat produsul: {product.name}")

    def display_all_products(self):
        if not self.products:
            print("Inventarul este gol.")
        else:
            print("\n=== Inventar ===")
            for product in self.products:
                product.display_info()
                print("-" * 30)

    def total_inventory_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        print(f"Valoarea totală a inventarului: {total} RON")
        return total


def remove_product_by_name(self, name):
    for p in self.products:
        if p.name.lower() == name.lower():
            self.products.remove(p)
            print(f"Produsul '{name}' a fost eliminat.")
            return
    print(f"Produsul '{name}' nu a fost găsit.")
