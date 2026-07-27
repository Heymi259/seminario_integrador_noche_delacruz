const trim      = (s: string): string => s.trim();
const aMinusculas = (s: string): string => s.toLowerCase();
const capitalizar = (s: string): string =>
  s.charAt(0).toUpperCase() + s.slice(1);
const quitarEspacios = (s: string): string => s.replace(/\s+/g, "_");

// Encadenar transformaciones manualmente
function normalizarUsuario(nombre: string): string {
  return quitarEspacios(capitalizar(aMinusculas(trim(nombre))));
}

const entradas = ["  ANA GARCÍA  ", " luis rodríguez", "PEDRO  LÓPEZ "];
entradas.forEach((e) => console.log(normalizarUsuario(e)));
// Ana_garcía
// Luis_rodríguez
// Pedro__lópez  (doble espacio interno → doble guión)