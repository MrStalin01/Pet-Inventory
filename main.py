import tkinter as tk
from tkinter import messagebox


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

ventana.mainloop()
