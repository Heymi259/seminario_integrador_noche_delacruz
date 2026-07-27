// tipo-unknown.ts

function procesarDato(valor: unknown): string {


  if (typeof valor === "string") {

    return valor.toUpperCase();
  }

  if (typeof valor === "number") {

    return valor.toFixed(2);
  }

  if (typeof valor === "boolean") {
    return valor ? "Sí" : "No";
  }

  return "Tipo no reconocido";
}

console.log(procesarDato("hola"));   // HOLA
console.log(procesarDato(3.14159));  // 3.14
console.log(procesarDato(true));     // Sí
console.log(procesarDato(null));     // Tipo no reconocido