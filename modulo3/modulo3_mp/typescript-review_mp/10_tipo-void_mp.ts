// tipo-void.ts

function saludar(nombre: string): void {
  console.log(`Hola, ${nombre}!`);
}

saludar("Ana");

function duplicar(n: number): number {
  return n * 2;
}

const resultado = duplicar(5);
console.log(resultado); 