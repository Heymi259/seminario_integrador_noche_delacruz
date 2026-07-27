// Una función que busca por ID (number) o por nombre (string)
type Producto = { id: number; nombre: string; precio: number };

const catalogo: Producto[] = [
  { id: 1, nombre: "Laptop",  precio: 1200 },
  { id: 2, nombre: "Teclado", precio: 80   },
  { id: 3, nombre: "Monitor", precio: 350  },
];

// Sobrecargas
function buscar(id: number): Producto | undefined;
function buscar(nombre: string): Producto[];
// Implementación
function buscar(criterio: number | string): Producto | Producto[] | undefined {
  if (typeof criterio === "number") {
    return catalogo.find((p) => p.id === criterio);
  }
  const termino = criterio.toLowerCase();
  return catalogo.filter((p) => p.nombre.toLowerCase().includes(termino));
}

// TypeScript sabe el retorno exacto por la firma elegida
const porId   = buscar(2);             // Producto | undefined
const porNombre = buscar("o");         // Producto[]

console.log(porId);
// { id: 2, nombre: 'Teclado', precio: 80 }

console.log(porNombre);
// [ { id: 2, nombre: 'Teclado', ... }, { id: 3, nombre: 'Monitor', ... } ]