from types import NoneType


MAX_INTENTOS = 3
nombre="Juan"
edad=30
estatura=1.75
activo=True
nulo=None
print(nombre, "tipo:", type(nombre))
print(edad, "tipo:", type(edad))
print(estatura, "tipo:", type(estatura))
print(activo, "tipo:", type(activo))
print(nulo, "tipo:", type(nulo))


nombre_apellido = "Juan Perez"
edad_trabajador = 30
altura_trabajador = 1.75
trabajador_activo: bool = True
nulo_trabajador: NoneType = None

print(nombre_apellido, "tipo:", type(nombre_apellido))
print(edad_trabajador, "tipo:", type(edad_trabajador))  
print(altura_trabajador, "tipo:", type(altura_trabajador))
print(trabajador_activo, "tipo:", type(trabajador_activo))
print(nulo_trabajador, "tipo:", type(nulo_trabajador))