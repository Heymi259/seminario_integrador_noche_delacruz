type CodigoHTTP = 200 | 400 | 401 | 403 | 404 | 500;

function manejarRespuesta(codigo: CodigoHTTP, datos?: string): void {
  if (codigo === 200) {
    console.log(`Éxito: ${datos ?? "sin datos"}`);
    return; // return vacío en void
  }
  procesarError(codigo); // never — el flujo no sigue
}

function procesarError(codigo: CodigoHTTP): never {
  const mensajes: Partial<Record<CodigoHTTP, string>> = {
    400: "Solicitud inválida",
    401: "No autenticado",
    403: "Sin permisos",
    404: "Recurso no encontrado",
    500: "Error interno del servidor",
  };
  throw new Error(`HTTP ${codigo}: ${mensajes[codigo] ?? "error desconocido"}`);
}

manejarRespuesta(200, "usuario cargado");  // Éxito: usuario cargado
// manejarRespuesta(404);                 // Lanza Error: HTTP 404: Recurso no encontrado