// tipos-string.ts
const nombre:    string = "Ana García";
const saludo:    string = `Hola, ${nombre}`;
const vacia:     string = "";
const comillas:  string = 'También con comillas simples';

console.log(nombre);
console.log(saludo);
console.log(`La cadena vacía tiene longitud: ${vacia.length}`);


console.log(nombre.toUpperCase());      
console.log(nombre.toLowerCase());      
console.log(nombre.includes("García")); 
console.log(nombre.split(" "));         