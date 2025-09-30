from product import Product
from typing import Optional

FILENAME = "inventario.txt"

def confirm_action(prompt: str) -> bool:
    while True:
        choice = input(f"\n{prompt} [s/n]: ").strip().lower()
        if choice in ['s', 'si']:
            return True
        elif choice in ['n', 'no']:
            print("Operación cancelada.")
            return False
        else:
            print("Respuesta no válida. Por favor, ingrese 's' para sí o 'n' para no.")

def load_products() -> list[Product]:
    products = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        name = parts[0].strip()
                        price = parts[1].strip()
                        quantity = parts[2].strip()
                        size = parts[3].strip()
                        products.append(Product(name, price, quantity, size))
    except FileNotFoundError:
        pass
    return products

def save_products(products: list[Product]):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for product in products:
            file.write(f"{product.name.strip()},{product.price.strip()},{product.quantity.strip()},{product.size.strip()}\n")

def find_and_select_product(products: list[Product], action_prompt: str) -> Optional[Product]:
    search_term = input(f"Ingrese el nombre (o parte) del producto a {action_prompt}: ").strip().lower()
    if not search_term:
        print("\nError: El término de búsqueda no puede estar vacío.")
        return None

    found_products = [p for p in products if search_term in p.name.lower()]

    if not found_products:
        print(f"\nNo se encontraron productos que coincidan con '{search_term}'.")
        return None
    
    if len(found_products) == 1:
        print(f"\nProducto encontrado: {found_products[0]}")
        return found_products[0]

    print(f"\nSe encontraron {len(found_products)} coincidencias. Por favor, elija uno:")
    for i, product in enumerate(found_products, 1):
        print(f"{i}. {product}")
    print("0. Cancelar")

    while True:
        try:
            choice = int(input("Su elección: ").strip())
            if choice == 0:
                print("Operación cancelada.")
                return None
            if 1 <= choice <= len(found_products):
                return found_products[choice - 1]
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")