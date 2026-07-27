# encapsulamiento_novafit.py

class SocioNovaFit:
    def __init__(self, nombre, saldo_inicial=0):
        self.nombre = nombre
        self.__saldo = saldo_inicial
        self.__activo = True
        self.__historial = []
        self.__registrar(f"Socio registrado con saldo inicial de ${saldo_inicial}")

    # GETTERS (propiedades)
    @property
    def saldo(self):
        return self.__saldo

    @property
    def activo(self):
        return self.__activo

    @property
    def historial(self):
        return list(self.__historial)

    # MÉTODOS PRINCIPALES
    def pagar_membresia(self, monto):
        if monto <= 0:
            raise ValueError("El pago debe ser mayor a 0")

        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente para pagar la membresía")

        self.__saldo -= monto
        self.__registrar(f"Pago de membresía: -${monto}")
        return self

    def recargar_saldo(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")

        self.__saldo += monto
        self.__registrar(f"Recarga de saldo: +${monto}")
        return self

    def suspender(self):
        self.__activo = False
        self.__registrar("Membresía suspendida")

    def activar(self):
        self.__activo = True
        self.__registrar("Membresía activada")

    # MÉTODO PRIVADO
    def __registrar(self, evento):
        from datetime import datetime
        hora = datetime.now().strftime("%H:%M:%S")
        self.__historial.append(f"[{hora}] {evento}")

    def __str__(self):
        return f"Socio({self.nombre}: ${self.__saldo})"


# USO DEL SISTEMA NOVAFIT
s1 = SocioNovaFit("Heymi", 100)
s2 = SocioNovaFit("Carlos", 50)

s1.recargar_saldo(50).pagar_membresia(30)
s1.suspender()

s2.recargar_saldo(100).pagar_membresia(40)

print(s1)
print(s2)

print(f"Saldo de {s1.nombre}: ${s1.saldo}")

print("\nHistorial de Heymi:")
for h in s1.historial:
    print(h)