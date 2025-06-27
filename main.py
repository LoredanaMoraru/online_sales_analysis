from product import Product
from product_manager import ProductManager

# Instanțiem ProductManager
manager = ProductManager()

# Adăugăm produse fictive
p1 = Product("Televizor", 2200, 2)
p2 = Product("Tabletă", 1400, 7)
p3 = Product("Imprimantă", 630, 3)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Afișăm inventarul
manager.display_all_products()
<<<<<<< HEAD
=======

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

>>>>>>> add-cart-functionality
