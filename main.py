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
