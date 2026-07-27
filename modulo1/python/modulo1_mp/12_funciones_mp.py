print("=== Funciones en NovaFit ===")

# Función básica
def bienvenida():
    print("¡Bienvenido a NovaFit!")

bienvenida()


# Función con parámetros
def saludar_socio(nombre):
    print(f"¡Hola {nombre}, bienvenido a NovaFit!")

saludar_socio("Heymi")
saludar_socio("Carlos")


# Función con retorno
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

imc = calcular_imc(65, 1.65)
print(f"IMC: {imc:.2f}")


# Parámetros por posición y por nombre
def presentar_socio(nombre, edad, objetivo):
    print(f"Socio: {nombre}, Edad: {edad}, Objetivo: {objetivo}")

presentar_socio("Heymi", 25, "Ganar masa muscular")
presentar_socio(nombre="Carlos", edad=30, objetivo="Perder peso")


# Valores por defecto
def registrar_membresia(nombre, plan="Mensual"):
    print(f"Socio: {nombre} - Plan: {plan}")

registrar_membresia("Heymi")
registrar_membresia("Carlos", "Anual")


# *args
def sumar_calorias(*calorias):
    print(f"Calorías registradas: {calorias}")
    return sum(calorias)

print("Total calorías:", sumar_calorias(300, 450, 250))


# Combinación de parámetros
def mostrar_rutina(nombre_rutina, *ejercicios):
    print(f"Rutina: {nombre_rutina}")
    for ejercicio in ejercicios:
        print("-", ejercicio)

mostrar_rutina(
    "Piernas",
    "Sentadillas",
    "Prensa",
    "Peso Muerto"
)


# **kwargs
def crear_perfil(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

crear_perfil(
    nombre="Heymi",
    edad=25,
    objetivo="Tonificar"
)


# Todos los tipos de parámetros
def configurar_gimnasio(nombre, *salas, abierto=True, **extras):
    print(f"Gimnasio: {nombre}")
    print(f"Salas: {salas}")
    print(f"Abierto: {abierto}")
    print(f"Extras: {extras}")

configurar_gimnasio(
    "NovaFit",
    "Cardio",
    "Pesas",
    abierto=True,
    wifi=True,
    parqueadero=True
)


# Múltiples valores de retorno
def peso_min_max(pesos):
    return min(pesos), max(pesos)

minimo, maximo = peso_min_max([65, 72, 58, 80, 69])

print("Peso mínimo:", minimo)
print("Peso máximo:", maximo)


# Retornar diccionario
def analizar_pesos(pesos):
    total = sum(pesos)
    cantidad = len(pesos)

    return {
        "total": total,
        "promedio": total / cantidad if cantidad > 0 else 0,
        "minimo": min(pesos) if pesos else None,
        "maximo": max(pesos) if pesos else None,
        "cantidad": cantidad
    }

datos = [65, 72, 58, 80, 69]
estadisticas = analizar_pesos(datos)

print("Promedio:", estadisticas["promedio"])
print("Mínimo:", estadisticas["minimo"])
print("Máximo:", estadisticas["maximo"])


# Funciones lambda
duplicar_peso = lambda peso: peso * 2
print(duplicar_peso(50))

calcular_total = lambda mensualidad, meses: mensualidad * meses
print(calcular_total(30, 12))