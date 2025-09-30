from inventory_utils import load_products

def find_product_by_name():
    print("\n--- Buscar Producto por Nombre ---")
    try:
        search_term = input("Ingrese el nombre o parte del nombre a buscar: ").strip().lower()
        
        if not search_term:
            raise ValueError("Debe ingresar un término de búsqueda.")
        
        products = load_products()
        
        found_products = [p for p in products if search_term in p.name.lower()]

        if found_products:
            print(f"\nSe encontraron {len(found_products)} productos que coinciden con '{search_term}':")
            for product in found_products:
                print(f"- {product}")
        else:
            print(f"\nNo se encontraron productos que coincidan con '{search_term}'.")
            
    except ValueError as e:
        print(f"\nError: {str(e)}")
    except Exception as e:
        print(f"\nError inesperado al buscar productos: {str(e)}")