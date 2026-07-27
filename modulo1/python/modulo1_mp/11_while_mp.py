print("=== Ciclos WHILE - NovaFit ===")

print("While básico")

dia = 1
while dia <= 5:
    print(f"Día de entrenamiento {dia}")
    dia += 1


print("\nRegistro de actividades")

actividad = ""
while actividad != "salir":
    actividad = input("Ingrese una actividad (o 'salir' para terminar): ")
    print("Actividad registrada:", actividad)


print("\nPago de membresías")

cantidad = int(input("¿Cuántas membresías desea registrar? "))

total = 0
contador = 0

while contador < cantidad:
    precio = float(input(f"Precio de la membresía {contador + 1}: "))
    total += precio
    contador += 1

print("Total recaudado: $", total)

if total >= 100:
    print("Se alcanzó la meta de ventas del día")
else:
    print("Aún no se alcanza la meta de ventas")