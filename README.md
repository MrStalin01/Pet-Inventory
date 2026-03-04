# Pet-Inventory 📦
-         Excel con PANDAS que valide la estructura y los datos, se introducen con Tkinter
La idea principal es crear una simulación de inventario para una tienda online con stock para la aplicación de PetMatch, un programa el cual se pueda organizar el inventario de la tienda y poder actualizar, añadir o borrar productos del stock con Pandas y Tkinter usando excel como base de datos.

<img src="./screenshots/Añadir.png" width=29% style="margin-right: 20px;">
<img src="./screenshots/menu.png" width=29% style="margin-right: 20px;">

# Excel.py

La clase la cual servira para desde ahí se pueda cargar y guardar en excel usando pandas todos los datos que introducimos desde la main, con un control de errores de códigos (ID de producto) duplicados o posibles errores de carga como “PermissionError” que ocurre cuando tenemos Excel abierto. 
El index=False es para que se vea mejor así evitando añadir columnas extras que no se necesitan.

Al momento de carga verifica si existe el archivo excel, si no existe lee el excel y hace una comprobación por cada columna que debería tener la tabla, si no existe la crea vacía. Esto se hace por si alguien borró una columna del Excel manualmente.

# Productos.py

Después la clase en la que creamos cada categoria y animales permitidos y su validación. 
Lo primero haciendo listas de Animales ["perro", "gato", "pajaro", "roedor", "pez", "reptil"] y Categorias ["alimentacion", "juguetes", "higiene", "accesorios", "salud"] que serviran como las opciones permitidas y poder usarlas en la main como menu desplegable.
Y por ultimo una función de validación de cada categoria hasta llegar animales y categorias la cual se validaria de distinta manera por si el usuario introduce un animal no valido.

# Main.py

La clase principal, aqui donde abririamos nuestro programa usando tkinter y pandas, ya que creariamos una función para cada una de las opciones de agregar(), borrar() y editar/ver().

Lo primero una función para abrir_menu() el Inventory y poder seleccionar la opcion de Agregar, eliminar y ver/editar. 

abrir_agregar():
Global permite modificar la tabla y se diseña la nueva ventana.
Campos de texto: "Codigo", "Producto", "Precio", "Stock" y se guarda en datos {}.
Desplegables: "animal" y "categoria" se guarda en su propia variable.
Todo es verificado por si hay un campo sin rellenar o mal introducido, si pasa la validación se guarda en Excel y limpia los campos.

# Dependecias ⚙️
-         pip install pandas openpyxl

tkinter -> viene incluido con python.
pandas -> manejo de tablas de datos.
openpyxl -> necesario para que pandas pueda leer y escribir archivos Excel.
