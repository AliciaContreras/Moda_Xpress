from inventory_utils import load_products

def find_product_by_name():
    print("\n Buscar producto por nombre")
    try:
        name=input("Nombre: ")
        products=load_products()
        if not name:
            raise ValueError("El nombre no puede estar vacío")
        
        products=load_products()
        product_found=None
        for product in products:
            if product.name.lower()==name.lower():
                product_found=product
                break
        if product_found:
            print(f"\n Producto '{product_found.name}' encontrado:\n")

if __name__=="__main__":
    find_product_by_name()