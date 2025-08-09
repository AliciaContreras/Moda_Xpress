from inventory_utils import load_products
from product import Product

def view_all_products():
    print("\n Inventario completo de Moda Xpress")
    try:
        products=load_products()
        if not products:
            print("No hay productos en el inventario")
            return
        
        for product in products:
            product.display_details()
    except (IOError, OSError) as e:
        print(f"Error de E/S al acceder al archivo de inventario: {str(e)}")
    except ValueError as e:
        print(f"Error en el formato de los datos del inventario: {str(e)}")
        
if __name__=="__main__":
    view_all_products()
