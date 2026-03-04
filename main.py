import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os

from Productos import validar_producto, Animales, Categorias
from excel import guardar_excel, cargar_excel, COLUMNAS, ARCHIVO_EXCEL

tabla_inventario = cargar_excel()
guardar_excel(tabla_inventario)



def abrir_menu():
    ventana = tk.Tk()
    ventana.title("Inventario PetMatch - Menú")
    ventana.geometry("300x250")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Inventario PetMatch", font=("Arial", 16, "bold")).pack(pady=20)

    tk.Button(
        ventana, text="Agregar Producto",
        command=lambda: [ventana.destroy(), abrir_agregar()]
    ).pack(pady=5)

    tk.Button(
        ventana, text="Eliminar Producto",
        command=lambda: [ventana.destroy(), abrir_eliminar()]
    ).pack(pady=5)

    tk.Button(
        ventana, text="Ver / Editar Inventario",
        command=lambda: [ventana.destroy(), abrir_inventario()]
    ).pack(pady=5)

    ventana.mainloop()


def abrir_agregar():
    global tabla_inventario

    ventana = tk.Tk()
    ventana.title("Agregar Producto")
    ventana.geometry("350x380")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Agregar Producto", font=("Arial", 13, "bold")).pack(pady=8)

    datos = {}
    for campo in ["Codigo", "Producto", "Precio", "Stock"]:
        tk.Label(ventana, text=campo).pack()
        entry = tk.Entry(ventana, width=28)
        entry.pack(pady=1)
        datos[campo] = entry

    tk.Label(ventana, text="Animal").pack()
    animalDesplegable = ttk.Combobox(
        ventana, width=26, state="readonly",
        values=[a.capitalize() for a in Animales]
    )
    animalDesplegable.pack(pady=1)

    tk.Label(ventana, text="Categoria").pack()
    categoriaDesplegable = ttk.Combobox(
        ventana, width=26, state="readonly",
        values=[c.capitalize() for c in Categorias]
    )
    categoriaDesplegable.pack(pady=1)

    def confirmar():
        global tabla_inventario

        codigo    = datos["Codigo"].get().strip()
        producto  = datos["Producto"].get().strip()
        animal    = animalDesplegable.get().lower()
        categoria = categoriaDesplegable.get().lower()

        if not animal:
            messagebox.showwarning("El Animal", "Selecciona un animal", parent=ventana)
            return
        if not producto:
            messagebox.showwarning("El Producto", "Selecciona un producto", parent=ventana)
            return

        try:
            stock  = int(datos["Stock"].get())
            precio = float(datos["Precio"].get())
        except ValueError:
            messagebox.showerror("Error", "Stock debe ser entero y Precio decimal", parent=ventana)
            return

        nuevo = {
            "Codigo": codigo, "Producto": producto,
            "Animal": animal, "Categoria": categoria,
            "Stock": stock,   "Precio": precio
        }

        tabla_inventario = pd.concat(
            [tabla_inventario, pd.DataFrame([nuevo])],
            ignore_index=True
        )

        errores = validar_producto(tabla_inventario)
        if errores:
            tabla_inventario = tabla_inventario.iloc[:-1].reset_index(drop=True)
            messagebox.showwarning("Error de validación", "\n".join(errores), parent=ventana)
        else:
            guardar_excel(tabla_inventario)
            messagebox.showinfo("Correcto", f"'{producto}' añadido y guardado en Excel", parent=ventana)
            for e in datos.values():
                e.delete(0, tk.END)

    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

    tk.Button(frame_botones, text="Añadir",
              command=confirmar).pack(side="left", padx=5)
    tk.Button(frame_botones, text="Menú", width=12,
              command=lambda: [ventana.destroy(), abrir_menu()]).pack(side="left", padx=5)

    ventana.mainloop()


    def abrir_eliminar():
        pass
    def abrir_inventario():
        pass

if __name__ == "__main__":
    abrir_menu()