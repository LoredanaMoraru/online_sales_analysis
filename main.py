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
