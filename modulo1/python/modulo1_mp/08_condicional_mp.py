print("Condicionales en NovaFit")

# IF SIMPLE
print("If simple")

cupos_disponibles = 5

if cupos_disponibles > 0:
    print("Hay cupos disponibles para la clase")


# IF ELSE
print("If else - dos caminos")

dias_membresia = 20

if dias_membresia > 0:
    print("Membresía activa")
else:
    print("Membresía vencida")


# IF CON MÚLTIPLES CONDICIONES
print("If múltiples condiciones")

imc = 27

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Peso normal")
else:
    print("Sobrepeso")


# IF ANIDADO
print("If condiciones anidadas")

socio_registrado = True
membresia_activa = False

if socio_registrado:
    if membresia_activa:
        print("Acceso permitido al gimnasio")
    else:
        print("La membresía está vencida")
else:
    print("Socio no registrado")