from inventory_utils import load_products

def find_product_by_name():
    print("\nBuscar producto por nombre")
    try:
        search_term = input("Ingrese el nombre o parte del nombre: ").strip().lower()
        
        if not search_term:
            raise ValueError("Debe ingresar un término de búsqueda")
        
        products = load_products()
        
        found_products = []
        for product in products:
            if search_term in product.name.lower():
                found_products.append(product)
        

        if found_products:
            print(f"\nSe encontraron {len(found_products)} productos que coinciden con '{search_term}':")
            for i, product in enumerate(found_products, 1):
                print(f"\nProducto {i}:")
                product.display_details()
        else:
            print(f"\nNo se encontraron productos que coincidan con '{search_term}'")
            
    except ValueError as e:
        print(f"\nError: {str(e)}")
    except Exception as e:
        print(f"\nError inesperado al buscar productos: {str(e)}")

if __name__ == "__main__":
    find_product_by_name()