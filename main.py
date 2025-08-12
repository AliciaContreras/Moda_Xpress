from add_product import add_new_product
from find_product import find_product_by_name
from view_inventory import view_all_products
from delete_product import delete_product
from modify_product import modify_product

def display_menu():
    print("\n Sistema de inventario de Moda Xpress")
    print("1. Añadir nuevo producto")
    print("2. Buscar producto por nombre")
    print("3. Ver inventario completo")
    print("4. Modificar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("-"*30)

def main():
    while True:
        display_menu()
        try:
            option=int(input("\nIngrese su opción: "))
            if option==1:
                add_new_product()
            elif option==2:
                find_product_by_name()
            elif option==3:
                view_all_products()
            elif option==4:
                modify_product()
            elif option==5:
                delete_product()
            elif option==6:
                print("\nGracias por usar el sistema. Hasta luego.")
                break
            else:
                print("\nOpción no válida. Por favor, ingrese una opción válida.")
        except ValueError:
            print("\nPor favor, ingrese un número válido.")

if __name__=="__main__":
    main()