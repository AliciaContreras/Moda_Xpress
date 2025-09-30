from product import Product
from inventory_utils import FILENAME, confirm_action

def add_new_product():
    print("\n--- Añadir Nuevo Producto ---")
    try:
        name = input("Nombre del producto: ").strip()
        price = input("Precio (ej: 15 USD): ").strip()
        quantity = input("Cantidad (ej: 50 unidades): ").strip()
        size = input("Talla (ej: M, 42, Talla Única): ").strip()
        
        if not all([name, price, quantity, size]):
            raise ValueError("Todos los campos son obligatorios.")
        
        new_product = Product(name, price, quantity, size)

        print(f"\nSe agregará el siguiente producto:\n-> {new_product}")
        if confirm_action("¿Confirma que desea agregar este producto?"):
            with open(FILENAME, "a", encoding="utf-8") as file:
                file.write(f"{name},{price},{quantity},{size}\n")
            print("\n¡Producto agregado exitosamente!")
        
    except ValueError as e:
        print(f"\nError: {str(e)}")
    except Exception as e:
        print(f"\nError inesperado al agregar el producto: {str(e)}")