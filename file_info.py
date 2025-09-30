import os
import datetime
from inventory_utils import FILENAME

def display_file_info():
    print("\n--- Información del Archivo de Inventario ---")
    try:
        if not os.path.exists(FILENAME):
            print(f"El archivo '{FILENAME}' no existe todavía.")
            return

        size_bytes = os.path.getsize(FILENAME)
        size_kb = size_bytes / 1024
        print(f"Tamaño del archivo: {size_bytes} bytes ({size_kb:.2f} KB)")

        mod_time_timestamp = os.path.getmtime(FILENAME)
        mod_time = datetime.datetime.fromtimestamp(mod_time_timestamp)
        print(f"Última modificación: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        print(f"No se pudo obtener la información del archivo: {e}")