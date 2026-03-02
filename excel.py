import pandas as pd
def guardar_excel(tabla_inventario, nombre_archivo="Inventario.xlsx"):
    try:
        tabla_inventario.to_excel(nombre_archivo, index=False) #index borra la columna extra para que quede mas limpio
        print(f"Archivo {nombre_archivo} guardado correctamente.")
    except Exception as e:
        print(f"Hubo un error al guardar: {e}")