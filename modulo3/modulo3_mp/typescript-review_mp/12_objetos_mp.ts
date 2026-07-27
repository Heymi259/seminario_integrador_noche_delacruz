// objetos.ts


const persona: { nombre: string; edad: number; activo: boolean } = {
  nombre: "Ana García",
  edad:   28,
  activo: true
};

console.log(persona.nombre);
console.log(persona.edad);

const producto: { nombre: string; precio: number; descuento?: number } = {
  nombre:  "Laptop",
  precio:  999
};

console.log(producto.descuento); // undefined — no se lanza error