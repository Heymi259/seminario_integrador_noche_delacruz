# clase-novafit.py

class Socio:
    # Atributo de clase (compartido por todos los socios)
    gimnasio = "NovaFit"

    # Constructor
    def __init__(self, nombre, edad, plan):
        self.nombre = nombre
        self.edad = edad
        self.plan = plan
        self.membresia_activa = True

    # Método de instancia
    def mostrar_informacion(self):
        return f"Socio: {self.nombre}, Edad: {self.edad}, Plan: {self.plan}"

    def entrenar(self):
        return f"{self.nombre} está entrenando en NovaFit 💪"

    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años.")

    def cancelar_membresia(self):
        self.membresia_activa = False
        print(f"La membresía de {self.nombre} ha sido cancelada.")

    # Representación amigable
    def __str__(self):
        return f"Socio({self.nombre}, {self.edad}, {self.plan})"

    # Representación técnica
    def __repr__(self):
        return f"Socio(nombre={self.nombre!r}, edad={self.edad!r}, plan={self.plan!r})"


# Crear objetos (socios de NovaFit)
ana = Socio("Ana García", 28, "Premium")
luis = Socio("Luis Pérez", 31, "Básico")

print(ana.mostrar_informacion())
print(luis.entrenar())

ana.cumplir_anios()
luis.cancelar_membresia()

print(str(ana))
print(repr(ana))

print(Socio.gimnasio)