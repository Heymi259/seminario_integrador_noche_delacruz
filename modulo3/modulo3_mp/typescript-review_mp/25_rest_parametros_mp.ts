function registrarEvento(tipo: string, ...detalles: string[]): void {
  const timestamp = new Date().toLocaleTimeString();
  const cuerpo = detalles.length > 0 ? ` | ${detalles.join(" · ")}` : "";
  console.log(`[${timestamp}] ${tipo.toUpperCase()}${cuerpo}`);
}

registrarEvento("inicio");

registrarEvento("login", "usuario: ana", "ip: 192.168.1.10");
registrarEvento("error", "módulo: pagos", "código: 503", "reintento: sí");
