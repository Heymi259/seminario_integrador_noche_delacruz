from types import NoneType

MAX_INTENTOS = 3

# Datos de un socio de NovaFit
nombre_socio = "Heymi"
edad_socio = 25
peso_socio = 65.5
membresia_activa = True
entrenador_asignado = None

print(nombre_socio, "tipo:", type(nombre_socio))
print(edad_socio, "tipo:", type(edad_socio))
print(peso_socio, "tipo:", type(peso_socio))
print(membresia_activa, "tipo:", type(membresia_activa))
print(entrenador_asignado, "tipo:", type(entrenador_asignado))

# Datos detallados del socio
nombre_completo_socio = "Heymi De La Cruz"
edad_cliente = 25
peso_cliente = 65.5
cliente_activo: bool = True
rutina_personalizada: NoneType = None

print(nombre_completo_socio, "tipo:", type(nombre_completo_socio))
print(edad_cliente, "tipo:", type(edad_cliente))
print(peso_cliente, "tipo:", type(peso_cliente))
print(cliente_activo, "tipo:", type(cliente_activo))
print(rutina_personalizada, "tipo:", type(rutina_personalizada))
