print("=== Ciclos FOR - NovaFit ===")

print("FOR básico")
for dia in range(1, 6):
    print(f"Día de entrenamiento {dia}")

print("\nRecorrer lista")
ejercicios = ["Sentadillas", "Press de banca", "Peso muerto", "Dominadas"]
for ejercicio in ejercicios:
    print(ejercicio)

print("\nControl de interrupciones")
for socio in range(1, 10):
    if socio == 3:
        continue  # Omite el socio 3
    if socio == 7:
        break     # Detiene el ciclo en el socio 7
    print(f"Socio {socio}")
else:
    print("Terminó el ciclo")

print("\nFOR con range y salto")
for repeticiones in range(2, 11, 2):
    print(f"{repeticiones} repeticiones")

print("\nFOR regresivo")
for segundos in range(10, 0, -1):
    print(segundos)

print("\nFOR con enumerate")
socios = ["Heymi", "Carlos", "Ana", "Pedro"]
for indice, socio in enumerate(socios):
    print(indice, socio)

print("\nFOR con zip")
edades = [25, 30, 22, 28]
for socio, edad in zip(socios, edades):
    print(f"{socio} - {edad} años")

print("\nFOR anidado")
for sala in range(1, 4):
    for maquina in range(1, 4):
        print(f"Sala {sala} - Máquina {maquina}")

print("\nPromedio de progreso del socio")

cantidad = int(input("Ingrese la cantidad de entrenamientos registrados: "))

suma = 0

for i in range(1, cantidad + 1):
    puntuacion = float(input(f"Puntuación del entrenamiento {i}: "))
    suma += puntuacion

promedio = suma / cantidad

print("Promedio de rendimiento:", promedio)

if promedio >= 7:
    print("Excelente progreso en NovaFit")
else:
    print("Debe mejorar su rendimiento")