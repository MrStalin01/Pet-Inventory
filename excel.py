import pandas as pd
def guardar_excel(tabla_inventario):
    try:
        # Validación de robustez (Punto 3 de la rúbrica)
        if tabla_inventario["codigo"].duplicated().any():
            print("Existen códigos duplicados.")
            return

        tabla_inventario.to_excel("Inventario.xlsx", index=False)#index borra la columna extra para que quede mas limpio
        print("Archivo guardado.")

    except PermissionError:
        print(f"El archivo 'Inventario.xlsx' está abierto. Ciérralo e intenta de nuevo.")
    except Exception as e:
        print(f"Error no se puede añadir: {e}")