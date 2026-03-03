import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os

from Productos import validar_producto
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

    entradas = {}
    for campo in COLUMNAS:
        tk.Label(ventana, text=campo).pack()
        entry = tk.Entry(ventana, width=28)
        entry.pack(pady=1)
        entradas[campo] = entry

    def confirmar():
        global tabla_inventario

        codigo    = entradas["Codigo"].get().strip()
        producto  = entradas["Producto"].get().strip()
        animal    = entradas["Animal"].get().strip()
        categoria = entradas["Categoria"].get().strip()

        try:
            stock  = int(entradas["Stock"].get())
            precio = float(entradas["Precio"].get())
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
            guardar_excel(tabla_inventario)  # ← guarda automáticamente
            messagebox.showinfo("Correcto", f"'{producto}' añadido y guardado en Excel", parent=ventana)
            for e in entradas.values():
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