from product import Product
from product_manager import ProductManager

# Instanțiem ProductManager
manager = ProductManager()

# Adăugăm produse fictive
p1 = Product("Laptop", 3200, 5)
p2 = Product("Telefon", 2500, 10)
p3 = Product("Casti", 300, 15)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Afișăm inventarul
manager.display_all_products()

# Afișăm valoarea totală
manager.total_inventory_value()


from cart import Cart
import random

# Creare instanță Cart
cart = Cart()

# Selectăm 3 produse aleatoriu din inventar
if len(manager.products) >= 3:
    produse_random = random.sample(manager.products, 3)
    for produs in produse_random:
        cart.add_to_cart(produs)
else:
    print("Nu există suficiente produse pentru a umple coșul.")

# Afișare coș și valoare totală
cart.display_cart()
cart.calculate_total()

