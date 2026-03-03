import pandas as pd
import os

ARCHIVO_EXCEL = "Inventario.xlsx"

COLUMNAS = ["Codigo", "Producto", "Animal", "Categoria", "Stock", "Precio"]

def guardar_excel(tabla_inventario):
    try:
        if tabla_inventario["Codigo"].duplicated().any():
            print("Existen códigos duplicados.")
            return

        tabla_inventario.to_excel(ARCHIVO_EXCEL, index=False)
        print("Archivo guardado correctamente.")

    except PermissionError:
        print("El archivo está abierto. Ciérralo e intenta de nuevo.")
    except Exception as e:
        print(f"Error al guardar: {e}")


def cargar_excel():
    if os.path.exists(ARCHIVO_EXCEL):
        try:
            df = pd.read_excel(ARCHIVO_EXCEL)
            for col in COLUMNAS:
                if col not in df.columns:
                    df[col] = ""
            return df[COLUMNAS]
        except Exception as e:
            print(f"Error al cargar: {e}")

    return pd.DataFrame(columns=COLUMNAS)