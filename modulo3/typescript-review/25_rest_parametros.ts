function registrarEvento(tipo: string, ...detalles: string[]): void {
  const timestamp = new Date().toLocaleTimeString();
  const cuerpo = detalles.length > 0 ? ` | ${detalles.join(" · ")}` : "";
  console.log(`[${timestamp}] ${tipo.toUpperCase()}${cuerpo}`);
}

registrarEvento("inicio");
// [10:05:01] INICIO

registrarEvento("login", "usuario: ana", "ip: 192.168.1.10");
// [10:05:02] LOGIN | usuario: ana · ip: 192.168.1.10

registrarEvento("error", "módulo: pagos", "código: 503", "reintento: sí");
// [10:05:03] ERROR | módulo: pagos · código: 503 · reintento: sí