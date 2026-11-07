productos = [
    "Arroz", "Leche", "Pan", "Huevos", "Azucar",
    "Cafe", "Aceite", "Pasta", "Galletas", "Queso"
]

precios = [4000, 3500, 2000, 12000, 4500,
           15000, 9000, 3000, 2500, 18000]

cantidades = [20, 15, 30, 10, 12, 8, 7, 25, 18, 4]

ventas = []


print("===== INVENTARIO DE LA TIENDA =====")

for i in range(len(productos)):
    print(
        productos[i],
        "| Precio:", precios[i],
        "| Cantidad:", cantidades[i]
    )


total_inventario = 0

for i in range(len(productos)):
    total_inventario += precios[i] * cantidades[i]

print("\nValor total del inventario:", total_inventario, "pesos")


indice_caro = precios.index(max(precios))
indice_barato = precios.index(min(precios))

print("Producto mas caro:", productos[indice_caro])
print("Producto mas barato:", productos[indice_barato])


poco_stock = []

for i in range(len(productos)):
    if cantidades[i] < 5:
        poco_stock.append(productos[i])

print("\nProductos con menos de 5 unidades:", poco_stock)


productos_caros = []

for i in range(len(productos)):
    if precios[i] > 50000:
        productos_caros.append(productos[i])

print("Productos de mas de 50000 pesos:", productos_caros)


busqueda = input("\n¿Qué producto deseas buscar?: ")
encontrado = False

for i in range(len(productos)):
    if productos[i].lower() == busqueda.lower():
        print("Precio:", precios[i])
        print("Cantidad disponible:", cantidades[i])
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")


vender = input("\n¿Deseas registrar una venta? (si/no): ")

if vender.lower() == "si":
    nombre = input("Nombre del producto: ")
    encontrado = False

    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            encontrado = True

            unidades = int(input("Cantidad que deseas vender: "))

            if unidades <= 0:
                print("La cantidad debe ser mayor que cero.")
            elif unidades <= cantidades[i]:
                cantidades[i] -= unidades
                total_venta = precios[i] * unidades

                ventas.append(total_venta)

                print("Venta realizada correctamente.")
                print("Dinero recibido:", total_venta, "pesos")
                print("Unidades restantes:", cantidades[i])
            else:
                print("No hay suficientes unidades disponibles.")

            break

    if not encontrado:
        print("Producto no encontrado.")


recibir = input("\n¿Deseas recibir nueva mercancia? (si/no): ")

if recibir.lower() == "si":
    nombre = input("Nombre del producto: ")
    encontrado = False

    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            unidades = int(input("Unidades que llegaron: "))

            if unidades > 0:
                cantidades[i] += unidades
                print("Inventario actualizado.")
            else:
                print("La cantidad debe ser positiva.")

            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")


cambiar = input("\n¿Deseas cambiar un precio? (si/no): ")

if cambiar.lower() == "si":
    nombre = input("Nombre del producto: ")
    encontrado = False

    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            nuevo_precio = float(input("Nuevo precio: "))

            if nuevo_precio > 0:
                precios[i] = nuevo_precio
                print("Precio actualizado.")
            else:
                print("El precio debe ser mayor que cero.")

            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")


agotados = 0
disponibles = 0

for cantidad in cantidades:
    if cantidad == 0:
        agotados += 1
    else:
        disponibles += 1

print("\nProductos con existencias:", disponibles)
print("Productos agotados:", agotados)


print("\n===== INFORME FINAL =====")

total_inventario = 0

for i in range(len(productos)):
    print(
        productos[i],
        "| Precio:", precios[i],
        "| Cantidad:", cantidades[i]
    )
    total_inventario += precios[i] * cantidades[i]

print("Valor actual del inventario:", total_inventario, "pesos")
print("Numero de ventas realizadas:", len(ventas))
print("Dinero total de ventas:", sum(ventas), "pesos")
