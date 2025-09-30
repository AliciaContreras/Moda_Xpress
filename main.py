from add_product import add_new_product
from find_product import find_product_by_name
from view_inventory import view_all_products
from delete_product import delete_product
from modify_product import modify_product
from backup_inventory import backup_inventory
from file_info import display_file_info

def display_menu():
    print("\n--- Sistema de Inventario de Moda Xpress ---")
    print("1. Añadir nuevo producto")
    print("2. Buscar producto por nombre")
    print("3. Ver inventario completo")
    print("4. Modificar producto")
    print("5. Eliminar producto")
    print("6. Ver información del archivo de inventario")
    print("7. Realizar copia de seguridad")
    print("8. Salir")
    print("-" * 42)

def main():
    while True:
        display_menu()
        try:
            option = input("\nIngrese su opción: ").strip()
            if not option:
                continue
            option = int(option)

            if option == 1:
                add_new_product()
            elif option == 2:
                find_product_by_name()
            elif option == 3:
                view_all_products()
            elif option == 4:
                modify_product()
            elif option == 5:
                delete_product()
            elif option == 6:
                display_file_info()
            elif option == 7:
                backup_inventory()
            elif option == 8:
                print("\nGracias por usar el sistema. ¡Hasta luego!")
                break
            else:
                print("\nOpción no válida. Por favor, ingrese un número del menú.")
        except ValueError:
            print("\nError: Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"\nHa ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    main()