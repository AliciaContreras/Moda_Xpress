from product import Product
from inventory_utils import FILENAME

def delete_product():
    print("\nEliminar producto")

    try:
        name = input("Nombre del producto a eliminar: ").strip()
        if not name:
            raise ValueError("El nombre del producto es obligatorio")
        
        products = []
        found = False
        
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) < 4:
                    print("Formato de producto inválido en el archivo.")
                    continue
                
                product_name = parts[0].strip()
                price = float(parts[1].replace(" USD", "").strip())
                quantity = int(parts[2].replace(" unidades", "").strip())
                size = parts[3].strip()
                
                if product_name.lower() == name.lower():
                    found = True
                    continue
                else:
                    product = Product(product_name, price, quantity, size)
                    products.append(product)
        
        if not found:
            print(f"Producto '{name}' no encontrado.")
            return
        
        with open(FILENAME, "w", encoding="utf-8") as file:
            for product in products:
                file.write(f"{product.name},{product.price} USD,{product.quantity} unidades,{product.size}\n")
        
        print(f"Producto '{name}' eliminado exitosamente.")
    
    except Exception as e:
        print(f"Error al eliminar el producto: {str(e)}")

if __name__ == "__main__":
    delete_product()
