from inventory_utils import load_products, save_products, find_and_select_product, confirm_action # Importamos

def modify_product():
    print("\n--- Modificar Producto ---")
    try:
        products = load_products()
        if not products:
            print("El inventario está vacío.")
            return

        product_to_modify = find_and_select_product(products, "modificar")

        if product_to_modify is None:
            return

        print("\nIngrese los nuevos datos (deje en blanco para no cambiar).")
        
        new_name = input(f"Nuevo nombre (actual: {product_to_modify.name}): ").strip()
        new_price = input(f"Nuevo precio (actual: {product_to_modify.price}): ").strip()
        new_quantity = input(f"Nueva cantidad (actual: {product_to_modify.quantity}): ").strip()
        new_size = input(f"Nueva talla (actual: {product_to_modify.size}): ").strip()

        if confirm_action("¿Confirma que desea aplicar estos cambios?"):
            if new_name:
                product_to_modify.name = new_name
            if new_price:
                product_to_modify.price = new_price
            if new_quantity:
                product_to_modify.quantity = new_quantity
            if new_size:
                product_to_modify.size = new_size
            
            save_products(products)
            print("\nProducto actualizado exitosamente.")

    except Exception as e:
        print(f"\nError inesperado al modificar el producto: {str(e)}")