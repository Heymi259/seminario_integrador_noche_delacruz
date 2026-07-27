// ternario.ts

const edad: number = 20;


let acceso: string;
if (edad >= 18) {
  acceso = "Permitido";
} else {
  acceso = "Denegado";
}


const acceso2: string = edad >= 18 ? "Permitido" : "Denegado";

console.log(acceso);   
console.log(acceso2);  
const nota: number = 7.5;
const calificacion = nota >= 5 ? "Aprobado" : "Suspenso";
console.log(`Nota: ${nota} — ${calificacion}`);


const resultado =
  nota >= 9 ? "Sobresaliente" :
  nota >= 7 ? "Notable"       :
  nota >= 5 ? "Aprobado"      : "Suspenso";

console.log(resultado);  // Notable