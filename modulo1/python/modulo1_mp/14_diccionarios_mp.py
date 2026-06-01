print("=== Diccionarios - NovaFit ===")

print("Crear un diccionario")

vacio = {}

socio = {
    "nombre": "Heymi",
    "edad": 25,
    "plan": "Premium",
    "objetivo": "Ganar masa muscular"
}

configuracion = dict(
    gimnasio="NovaFit",
    horario="06:00 - 22:00",
    capacidad=200
)

# Acceso
print(socio["nombre"])

# Modificar
socio["nombre"] = "Heymi De La Cruz"
print(socio["nombre"])

# Eliminar
del socio["edad"]
print(socio)

# Verificar existencia de claves
print("nombre" in socio)
print("peso" in socio)

# Métodos esenciales
print(socio.keys())
print(socio.values())
print(socio.items())

# Iterar el diccionario
for clave, valor in socio.items():
    print(f"{clave}: {valor}")