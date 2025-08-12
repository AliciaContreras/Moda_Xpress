from product import Product
from inventory_utils import FILENAME

def modify_product():
    print("\nModificar producto")

    try:
        name = input("Nombre del producto a modificar: ").strip()
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
                price = (parts[1].replace(" USD", "").strip())
                quantity = (parts[2].replace(" unidades", "").strip())
                size = parts[3].strip()
                product = Product(product_name, (price), (quantity), size)
                products.append(product)
                
                if product_name.lower() == name.lower():
                    print(f"Producto encontrado: {product}")
                    new_price = input("Nuevo precio (dejar en blanco para no cambiar): ").strip()
                    new_quantity = input("Nueva cantidad (dejar en blanco para no cambiar): ").strip()
                    new_size = input("Nuevo tamaño (dejar en blanco para no cambiar): ").strip()
                    
                    if new_price:
                        product.price = float(new_price)
                    if new_quantity:
                        product.quantity = int(new_quantity)
                    if new_size:
                        product.size = new_size
                    print(f"Producto modificado: {product}")
                    found = True
                    break
        if not found:
            print("Producto "{name}" no encontrado.")
            return
        
        with open(FILENAME, "w", encoding="utf-8") as file:
            for product in products:
                file.write(f"{product.name}, {product.price} USD, {product.quantity} unidades, {product.size}\n")
        print("Producto modificado exitosamente.")
        
    except ValueError as e:
        print(f"Error: {e}")
            
            
     