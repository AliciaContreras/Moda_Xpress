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
        
        new_product=Product(name, price, quantity, size)
        with open(FILENAME, "a", encoding="utf-8") as file:
            file.write(str(new_product) + "\n")
        print("Producto agregado exitosamente")
    except Exception as e:
        print(f"Error al agregar el producto: {str(e)}")

if __name__=="__main__":
    add_new_product()
