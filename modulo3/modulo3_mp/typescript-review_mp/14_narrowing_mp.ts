// narrowing.ts

function describir(valor: string | number | boolean): string {
  if (typeof valor === "string") {

    return `Texto en mayúsculas: ${valor.toUpperCase()}`;
  }

  if (typeof valor === "number") {

    return `Número al cuadrado: ${valor ** 2}`;
  }


  return valor ? "Verdadero" : "Falso";
}

console.log(describir("hola"));   // Texto en mayúsculas: HOLA
console.log(describir(5));        // Número al cuadrado: 25
console.log(describir(true));     // Verdadero

// También funciona con null
function procesarNombre(nombre: string | null): string {
  if (nombre === null) {
    return "Sin nombre";
  }
  // Aquí TypeScript sabe que nombre es string (descartó null)
  return nombre.trim().toUpperCase();
}

console.log(procesarNombre("  Ana García  "));  // ANA GARCÍA
console.log(procesarNombre(null));              // Sin nombre