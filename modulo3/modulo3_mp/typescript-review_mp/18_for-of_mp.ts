// for-of.ts

const nombres: string[] = ["Ana", "Luis", "Marta", "Carlos"];
const precios: number[] = [100, 250, 75, 320, 50];


for (const nombre of nombres) {
  console.log(`Hola, ${nombre}!`);

}

let total: number = 0;
for (const precio of precios) {
  total += precio;

}
console.log(`Total: ${total}€`);


for (const [indice, nombre] of nombres.entries()) {
  console.log(`${indice + 1}. ${nombre}`);
}