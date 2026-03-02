def guardar_excel(tabla_inventario):
    archivo = "Inventario.xlsx"

    # Exportamos el DataFrame al archivo Excel
    tabla_inventario.to_excel(archivo, index=False)

    print(f"Inventario actualizado correctamente en: {archivo}")
