# abstraccion_novafit.py
from abc import ABC, abstractmethod

# Clase abstracta: Equipos del gimnasio NovaFit
class Equipo(ABC):
    def __init__(self, nombre, color="negro"):
        self.nombre = nombre
        self.color = color

    @abstractmethod
    def uso_calorias(self) -> float:
        pass

    @abstractmethod
    def nivel_intensidad(self) -> float:
        pass

    # Método común para todos los equipos
    def describir(self) -> str:
        return (f"{self.nombre} ({self.color}) -> "
                f"calorías={self.uso_calorias():.2f}, "
                f"intensidad={self.nivel_intensidad():.2f}")


# Máquina de cardio
class Caminadora(Equipo):
    def __init__(self, minutos, velocidad, color="gris"):
        super().__init__("Caminadora", color)
        self.minutos = minutos
        self.velocidad = velocidad

    def uso_calorias(self):
        return self.minutos * self.velocidad * 3.5

    def nivel_intensidad(self):
        return self.velocidad * 2


# Máquina de fuerza
class Pesas(Equipo):
    def __init__(self, peso, repeticiones, color="negro"):
        super().__init__("Pesas", color)
        self.peso = peso
        self.repeticiones = repeticiones

    def uso_calorias(self):
        return self.peso * self.repeticiones * 0.5

    def nivel_intensidad(self):
        return self.peso / 10


# Bicicleta estática
class Bicicleta(Equipo):
    def __init__(self, tiempo, resistencia, color="rojo"):
        super().__init__("Bicicleta", color)
        self.tiempo = tiempo
        self.resistencia = resistencia

    def uso_calorias(self):
        return self.tiempo * self.resistencia * 4

    def nivel_intensidad(self):
        return self.resistencia * 1.5


# Polimorfismo: todos los equipos funcionan igual en el loop
equipos = [
    Caminadora(30, 6),
    Pesas(40, 12),
    Bicicleta(25, 5)
]

for e in equipos:
    print(e.describir())

calorias_totales = sum(e.uso_calorias() for e in equipos)
print(f"\nCalorías totales en NovaFit: {calorias_totales:.2f}")