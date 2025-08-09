from product import Product

FILENAME="inventario.txt"

def load_products() -> list[Product]:
    products=[]
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    parts=line.strip().split(",")
                    if len(parts)==4:
                        products.append(Product(parts[0], parts[1], parts[2], parts[3]))
    except FileNotFoundError:
        pass
    return products

def save_products(products: list[Product]):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for product in products:
            file.write(f"{product.name},{product.price},{product.quantity},{product.size}\n")
