import tkinter as tk
from tkinter import messagebox
import pandas as pd

from Productos import validar_producto
from excel import guardar_excel




tabla_inventario = pd.DataFrame(columns=[
   "Codigo",
   "Producto",
   "Animal",
   "Categoria",
   "Stock",
   "Precio"
])




def agregar_producto():


   global tabla_inventario


   codigo_producto = entrada_codigo.get()
   nombre_producto = entrada_producto.get()
   animal_producto = entrada_animal.get()
   categoria_producto = entrada_categoria.get()


   try:
       stock_producto = int(entrada_stock.get())
       precio_producto = float(entrada_precio.get())
   except:
       messagebox.showerror("Error", "Stock o precio incorrectos")
       return


   nuevo_producto = {
       "Codigo": codigo_producto,
       "Producto": nombre_producto,
       "Animal": animal_producto,
       "Categoria": categoria_producto,
       "Stock": stock_producto,
       "Precio": precio_producto
   }


   tabla_inventario = pd.concat(
       [tabla_inventario, pd.DataFrame([nuevo_producto])],
       ignore_index=True
   )


   errores = validar_producto(tabla_inventario)


   if errores:
       messagebox.showwarning(
           "Error",
           "\n".join(errores)
       )
   else:
       messagebox.showinfo("Correcto", "Producto añadido correctamente")


   limpiar_campos()




def guardar_inventario():
   guardar_excel(tabla_inventario)
   messagebox.showinfo("Guardado", "Excel creado correctamente")


def limpiar_campos():
   entrada_codigo.delete(0, tk.END)
   entrada_producto.delete(0, tk.END)
   entrada_animal.delete(0, tk.END)
   entrada_categoria.delete(0, tk.END)
   entrada_stock.delete(0, tk.END)
   entrada_precio.delete(0, tk.END)

#Tkinter
ventana = tk.Tk()
ventana.title("Inventario Tienda Animal")
ventana.geometry("400x400")

tk.Label(ventana, text="Codigo").pack()
entrada_codigo = tk.Entry(ventana)
entrada_codigo.pack()

tk.Label(ventana, text="Producto").pack()
entrada_producto = tk.Entry(ventana)
entrada_producto.pack()

tk.Label(ventana, text="Animal").pack()
entrada_animal = tk.Entry(ventana)
entrada_animal.pack()

tk.Label(ventana, text="Categoria").pack()
entrada_categoria = tk.Entry(ventana)
entrada_categoria.pack()

tk.Label(ventana, text="Stock").pack()
entrada_stock = tk.Entry(ventana)
entrada_stock.pack()

tk.Label(ventana, text="Precio").pack()
entrada_precio = tk.Entry(ventana)
entrada_precio.pack()

tk.Button(
   ventana,
   text="Añadir producto",
   command=agregar_producto
).pack(pady=5)


tk.Button(
   ventana,
   text="Guardar en Excel",
   command=guardar_inventario
).pack(pady=5
      )


ventana.mainloop()

