from product import Product
from inventory_utils import FILENAME

def backup_inventory():
    print("\nRealizando copia de seguridad del inventario")

    try:
        products = []
        
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
        
        backup_filename = "backup_inventory.txt"
        with open(backup_filename, "w", encoding="utf-8") as backup_file:
            for product in products:
                backup_file.write(f"{product.name}, {product.price} USD, {product.quantity} unidades, {product.size}\n")
        
        print(f"Copia de seguridad realizada exitosamente en {backup_filename}")

    except Exception as e:
        print(f"Error al realizar la copia de seguridad: {e}")

    finally:
        print("Proceso de copia de seguridad finalizado.")