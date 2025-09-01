import random

inventario = {
    'Tecnología': [{'nombre': 'Teléfonos móviles', 'cantidad': 5}, {'nombre': 'Auriculares', 'cantidad': 10}],
    'Hogar': [{'nombre': 'Sillas', 'cantidad': 8}, {'nombre': 'Mesas', 'cantidad': 4}],
    'Libros': [{'nombre': 'Comics', 'cantidad': 15}, {'nombre': 'Novelas', 'cantidad': 7}]
}

def vender_productos(num_ventas):
    """Simula la venta de varios productos."""
    print("--- Simulación de Venta ---")
    for i in range(num_ventas):
        categorias = list(inventario.keys())
        categoria_elegida = random.choice(categorias)
        productos = inventario[categoria_elegida]
        
        if not productos:
            print(f"[{i+1}] No hay productos en la categoría: {categoria_elegida}. Saltando...")
            continue

        producto_a_vender = random.choice(productos)
        
        print(f"[{i+1}] Vendiendo '{producto_a_vender['nombre']}' de la categoría '{categoria_elegida}'.")
        
        # Lógica de venta: si la cantidad es 1, se "saca" el producto.
        if producto_a_vender['cantidad'] == 1:
            productos.remove(producto_a_vender)
            print("Producto agotado.")
        else:
            producto_a_vender['cantidad'] -= 1
            print(f"Quedan {producto_a_vender['cantidad']} unidades.")

def reponer_producto(categoria, nombre, cantidad):
    """Añade o repone la cantidad de un producto en el inventario."""
    if categoria not in inventario:
        print(f"\nLa categoría '{categoria}' no existe.")
        return
        
    productos = inventario[categoria]
    # Buscar el producto existente
    producto_existente = next((p for p in productos if p['nombre'] == nombre), None)
    
    if producto_existente:
        producto_existente['cantidad'] += cantidad
        print(f"\n--- Reposición ---")
        print(f"Se repusieron {cantidad} unidades de '{nombre}'. Cantidad total: {producto_existente['cantidad']}.")
    else:
        # Añadir como nuevo producto
        productos.append({'nombre': nombre, 'cantidad': cantidad})
        print(f"\n--- Reposición ---")
        print(f"'{nombre}' se ha añadido a la categoría '{categoria}' con {cantidad} unidades.")

# Realizar 3 ventas aleatorias
vender_productos(3)

# Reponer un producto existente
reponer_producto('Tecnología', 'Auriculares', 5)

# Añadir un nuevo producto
reponer_producto('Hogar', 'Velas', 10)

print("\n--- Estado Final del Inventario ---")
print(inventario)