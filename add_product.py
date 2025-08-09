from product import Product
from inventory_utils import FILENAME

def add_new_product():
    print("\n Añadir nuevo producto")

    try:
        # Obtener y validar los datos del producto
        name = input("Nombre del producto: ").strip()
        
        # Validar y formatear el precio
        price = input("Precio (ej: 15 USD): ").strip()
        if not price.endswith("USD"):
            try:
                # Intentar convertir a número y agregar USD si no está presente
                float(price.split()[0])
                price = f"{price} USD"
            except (ValueError, IndexError):
                pass
        
        # Validar y formatear la cantidad
        quantity = input("Cantidad (ej: 50 unidades): ").strip()
        if not any(word in quantity.lower() for word in ["unidad", "unidades"]):
            try:
                # Si solo ingresaron el número, agregar "unidades"
                int(quantity.split()[0])
                quantity = f"{quantity} unidades"
            except (ValueError, IndexError):
                pass
        
        size = input("Talla (ej: M, L, 42, Talla Única): ").strip()
        
        # Validar que ningún campo esté vacío
        if not all([name, price, quantity, size]):
            raise ValueError("Todos los campos son obligatorios")
        
        # Crear el producto
        new_product = Product(name, price, quantity, size)
        
        # Guardar en el archivo con el formato correcto
        with open(FILENAME, "a", encoding="utf-8") as file:
            file.write(f"{name}, {price}, {quantity}, {size}\n")
            
        print("\nProducto agregado exitosamente!")
        
    except ValueError as e:
        print(f"\nError: {str(e)}")
    except Exception as e:
        print(f"\nError inesperado al agregar el producto: {str(e)}")

if __name__ == "__main__":
    add_new_product()
