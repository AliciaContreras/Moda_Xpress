from product import Product
from inventory_utils import FILENAME

def add_new_product():
    print("\n Añadir nuevo producto")

    try:
        name=input("Nombre: ")
        price=input("Precio: ")
        quantity=input("Cantidad: ")
        size=input("Talla: ")
        if not all([name, price, quantity, size]):
            raise ValueError("Todos los campos son obligatorios")
        
        # Create the product
        new_product=Product(name, price, quantity, size)
        # Save in CSV format to match load_products() expectations
        with open(FILENAME, "a", encoding="utf-8") as file:
            file.write(f"{name},{price},{quantity},{size}\n")
        print("Producto agregado exitosamente")
    except Exception as e:
        print(f"Error al agregar el producto: {str(e)}")

if __name__=="__main__":
    add_new_product()
