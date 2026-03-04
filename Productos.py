Animales = [
    "perro", "gato", "pajaro", "roedor", "pez", "reptil"
]
Categorias = [
    "alimentacion", "juguetes", "higiene", "accesorios", "salud"
]

def validar_producto(tabla_inventario):
    errores= []

    if tabla_inventario["Codigo"].duplicated().any():
        errores.append("Codigo repetido")

    if (tabla_inventario["Stock"] <= 0).any():
        errores.append("El stock no puede ser negativo")

    if(tabla_inventario["Precio"] <= 0).any():
        errores.append("El precio no puede ser negativo")

    animales_lower = [a.lower() for a in Animales]
    categorias_lower = [c.lower() for c in Categorias]

    for animal in tabla_inventario["Animal"]:
        if str(animal).lower() not in animales_lower:
            errores.append(f"Animal no válido: {animal}. Válidos: {', '.join(Animales)}")

    for categoria in tabla_inventario["Categoria"]:
        if str(categoria).lower() not in categorias_lower:
            errores.append(f"Categoría inválida: {categoria}. Válidas: {', '.join(Categorias)}")

    return errores