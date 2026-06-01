# Registro de un socio de NovaFit

nombre = input("Ingrese el nombre del socio: ")
print(f"¡Bienvenido a NovaFit, {nombre}!")

edad_str = input("Ingrese la edad del socio: ")
print(f"El socio tiene {edad_str} años")

edad = int(edad_str)
print(f"En 5 años tendrá {edad + 5} años")

peso_str = input("Ingrese el peso del socio (kg): ")
peso = float(peso_str)

print(f"{nombre} registra un peso de {peso} kg")