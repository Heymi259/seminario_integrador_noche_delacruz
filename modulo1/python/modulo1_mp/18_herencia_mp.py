# herencia_novafit.py

class EquipoGym:
    def __init__(self, nombre, marca, año):
        self.nombre = nombre
        self.marca = marca
        self.año = año
        self._uso = 0   # uso acumulado (protegido)

    def usar(self, minutos):
        self._uso += minutos
        return self

    def reiniciar_uso(self):
        self._uso = 0
        return self

    def __str__(self):
        return f"{self.nombre} {self.marca} ({self.año}) — Uso: {self._uso} min"


# HERENCIA: Cardio
class Caminadora(EquipoGym):
    def __init__(self, marca, año, velocidad_max):
        super().__init__("Caminadora", marca, año)
        self.velocidad_max = velocidad_max

    def correr(self):
        return f"{self.marca} Caminadora en uso 💨"

    def __str__(self):
        return f"{super().__str__()} | Velocidad máx: {self.velocidad_max} km/h"


# HERENCIA: Fuerza
class Pesas(EquipoGym):
    def __init__(self, marca, año, peso_max):
        super().__init__("Pesas", marca, año)
        self.peso_max = peso_max

    def levantar(self):
        return f"{self.marca} Pesas activadas 💪"

    def __str__(self):
        return f"{super().__str__()} | Peso máx: {self.peso_max} kg"


# HERENCIA: Cardio avanzado
class BicicletaElectrica(Caminadora):
    def __init__(self, marca, año, autonomia):
        super().__init__(marca, año, velocidad_max=50)
        self.__autonomia = autonomia
        self.__bateria = 100

    def cargar(self, porcentaje=100):
        self.__bateria = min(100, self.__bateria + porcentaje)
        return self

    @property
    def autonomia_restante(self):
        return self.__autonomia * self.__bateria / 100

    def __str__(self):
        return (f"{super().__str__()} | "
                f"Batería: {self.__bateria}% | "
                f"Autonomía: {self.autonomia_restante:.0f} km")


# USO DEL SISTEMA NOVAFIT
t1 = Caminadora("Technogym", 2023, 20)
p1 = Pesas("LifeFitness", 2022, 200)
b1 = BicicletaElectrica("ProFit", 2024, 120)

t1.usar(30)
p1.usar(45)
b1.usar(20)

print(t1)
print(p1)
print(b1)

# isinstance
print(isinstance(b1, BicicletaElectrica))  # True
print(isinstance(b1, Caminadora))          # True
print(isinstance(b1, EquipoGym))           # True

# MRO
print(BicicletaElectrica.__mro__)