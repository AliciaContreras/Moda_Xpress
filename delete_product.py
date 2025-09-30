from inventory_utils import load_products, save_products, find_and_select_product, confirm_action # Importamos

def delete_product():
    print("\n--- Eliminar Producto ---")
    try:
        products = load_products()
        if not products:
            print("El inventario está vacío.")
            return

        product_to_delete = find_and_select_product(products, "eliminar")

        if product_to_delete is None:
            return

        if confirm_action(f"¿Confirma que desea ELIMINAR PERMANENTEMENTE '{product_to_delete.name}'?"):
            updated_products = [p for p in products if p is not product_to_delete]
            save_products(updated_products)
            print(f"\nProducto '{product_to_delete.name}' eliminado exitosamente.")
    
    except Exception as e:
        print(f"\nError inesperado al eliminar el producto: {str(e)}")