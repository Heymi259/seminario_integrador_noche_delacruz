numero = int(input("Empleados: "))
ingreso = 0
total = 0

while ingreso < numero:
    total += float(input("Salario: "))
    ingreso += 1

print("Total:", total)
print("Gasto alto" if total >= 1000 else "Gasto controlado")