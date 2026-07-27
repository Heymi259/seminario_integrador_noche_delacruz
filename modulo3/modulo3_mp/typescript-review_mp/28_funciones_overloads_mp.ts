
type Producto = { id: number; nombre: string; precio: number };

const catalogo: Producto[] = [
  { id: 1, nombre: "Laptop",  precio: 1200 },
  { id: 2, nombre: "Teclado", precio: 80   },
  { id: 3, nombre: "Monitor", precio: 350  },
];


function buscar(id: number): Producto | undefined;
function buscar(nombre: string): Producto[];

function buscar(criterio: number | string): Producto | Producto[] | undefined {
  if (typeof criterio === "number") {
    return catalogo.find((p) => p.id === criterio);
  }
  const termino = criterio.toLowerCase();
  return catalogo.filter((p) => p.nombre.toLowerCase().includes(termino));
}

const porId   = buscar(2);             
const porNombre = buscar("o");         

console.log(porId);
console.log(porNombre);