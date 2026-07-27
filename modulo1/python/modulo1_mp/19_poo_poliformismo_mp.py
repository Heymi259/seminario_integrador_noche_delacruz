# polimorfismo_novafit.py

# CLASE BASE
class Notificacion:
    def __init__(self, socio, mensaje):
        self.socio = socio
        self.mensaje = mensaje

    def enviar(self):
        raise NotImplementedError("Debe implementarse en subclases")

    def __str__(self):
        return f"{self.__class__.__name__} → {self.socio}"


# NOTIFICACIÓN EMAIL
class NotificacionEmail(Notificacion):
    def __init__(self, socio, mensaje, asunto="NovaFit"):
        super().__init__(socio, mensaje)
        self.asunto = asunto

    def enviar(self):
        return f"📧 Email a {self.socio}: [{self.asunto}] {self.mensaje}"


# NOTIFICACIÓN SMS
class NotificacionSMS(Notificacion):
    MAX = 160

    def enviar(self):
        msg = self.mensaje[:self.MAX]
        return f"📱 SMS a {self.socio}: {msg}"


# NOTIFICACIÓN PUSH
class NotificacionPush(Notificacion):
    def enviar(self):
        return f"🔔 Push a {self.socio}: {self.mensaje[:50]}..."


# NOTIFICACIÓN WHATSAPP (extra realista)
class NotificacionWhatsApp(Notificacion):
    def enviar(self):
        return f"💬 WhatsApp a {self.socio}: {self.mensaje}"


# POLIMORFISMO: mismo método, distintos comportamientos
def enviar_notificaciones(lista):
    for n in lista:
        print(n.enviar())


# DATOS NOVAFIT
alertas = [
    NotificacionEmail("Heymi", "Tu membresía vence pronto", "Pago NovaFit"),
    NotificacionSMS("Carlos", "Tu clase empieza en 30 minutos"),
    NotificacionPush("Dispositivo-01", "Nueva rutina disponible"),
    NotificacionWhatsApp("Ana", "Promoción: 2x1 en mensualidad"),
]

print("=== Enviando notificaciones NovaFit ===")
enviar_notificaciones(alertas)


# ============================
# DUCK TYPING en NovaFit
# ============================

class ArchivoSociosLocal:
    def leer(self):
        return "datos de socios locales"

    def escribir(self, datos):
        print(f"Guardando socios localmente: {datos[:30]}...")


class ArchivoSociosNube:
    def leer(self):
        return "datos de socios en la nube"

    def escribir(self, datos):
        print(f"Sincronizando con nube: {datos[:30]}...")


class ArchivoSociosBD:
    def leer(self):
        return "datos de socios en base de datos"

    def escribir(self, datos):
        print(f"Actualizando BD: {datos[:30]}...")


def procesar_datos_socio(archivo):
    datos = archivo.leer()
    print(f"Procesando: {datos}")
    archivo.escribir(f"backup_{datos}")


print("\n=== Procesamiento de datos NovaFit ===")

for archivo in [ArchivoSociosLocal(), ArchivoSociosNube(), ArchivoSociosBD()]:
    procesar_datos_socio(archivo)