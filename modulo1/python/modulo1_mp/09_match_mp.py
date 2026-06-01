print("=== Sistema NovaFit ===")

accion = input("Acción (registrar/entrenar/pago): ")

match accion:
    case "registrar":
        print("Socio registrado correctamente")
    case "entrenar":
        print("Inicio de sesión de entrenamiento")
    case "pago":
        print("Procesando pago de membresía")
    case _:
        print(f"La acción '{accion}' no es válida")


print("\n=== Evaluación de Entrenamiento ===")

dias_entrenamiento = int(input("Ingrese los días entrenados esta semana: "))

match dias_entrenamiento:
    case n if n < 0:
        print(f"{n} no es una cantidad válida de días")
    case 0:
        print("No ha entrenado esta semana")
    case n if n % 2 == 0:
        print(f"Ha entrenado {n} días. Cantidad par de entrenamientos")
    case n:
        print(f"Ha entrenado {n} días. Cantidad impar de entrenamientos")