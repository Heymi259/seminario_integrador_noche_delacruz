// break-continue.ts

console.log("Buscar el primero mayor de 50:");
const valores: number[] = [23, 45, 12, 67, 34, 89, 56];

for (const v of valores) {
  if (v > 50) {
    console.log(`  Encontrado: ${v}`);
    break; 
  }
  console.log(`  ${v} no es mayor de 50`);
}

console.log("\nSolo números pares:");
for (let i = 1; i <= 10; i++) {
  if (i % 2 !== 0) continue;  // salta los impares
  console.log(`  ${i}`);
}


const datos: Array<number | null> = [1, null, 3, null, 5, 6];
let suma: number = 0;

for (const dato of datos) {
  if (dato === null) continue;  
  suma += dato;
}
console.log(`\nSuma ignorando null: ${suma}`);  // 15