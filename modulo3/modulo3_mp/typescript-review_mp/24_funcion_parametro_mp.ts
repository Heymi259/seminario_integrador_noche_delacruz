type Nivel = "info" | "warn" | "error";

function log(
  mensaje: string,
  nivel: Nivel = "info",
  timestamp?: boolean
): string {
  const prefijos: Record<Nivel, string> = {
    info:  "ℹ️  INFO ",
    warn:  "⚠️  WARN ",
    error: "❌ ERROR",
  };

  const hora = timestamp ? ` [${new Date().toISOString()}]` : "";
  return `${prefijos[nivel]}${hora}: ${mensaje}`;
}

console.log(log("Servidor iniciado"));

console.log(log("Memoria alta", "warn"));


console.log(log("Conexión perdida", "error", true));
