type Prioridad = "alta" | "media" | "baja";
type Tarea = { id: number; titulo: string; prioridad: Prioridad; horas: number };
function buscarTarea(id: number): Tarea | undefined;
function buscarTarea(prioridad: Prioridad): Tarea[];
function buscarTarea(criterio: number | Prioridad): Tarea | Tarea[] | undefined {
  if (typeof criterio === "number") {
    return tareas.find((t) => t.id === criterio);
  }
  return tareas.filter((t) => t.prioridad === criterio);
}

function crearTareas(prioridad: Prioridad = "media", ...titulos: string[]): Tarea[] {
  return titulos.map((titulo, i) => ({
    id: Date.now() + i,
    titulo,
    prioridad,
    horas: 0,
  }));
}

type AnalizadorTarea = (t: Tarea) => string;

const formatearTarea: AnalizadorTarea = (t) =>
  `[${t.prioridad.toUpperCase().padEnd(5)}] #${t.id} "${t.titulo}" (${t.horas}h)`;

function generarReporte(lista: Tarea[], analizar: AnalizadorTarea): void {
  console.log("=== Reporte de Tareas ===");
  lista.forEach((t) => console.log(analizar(t)));
  const totalHoras = lista.reduce((acc, t) => acc + t.horas, 0);
  console.log(`Total: ${lista.length} tareas · ${totalHoras}h estimadas`);
}

function crearAcumulador() {
  let total = 0;
  return {
    agregar: (horas: number): void => { total += horas; },
    obtener: (): number => total,
  };
}

function validarTarea(t: Tarea): void {
  if (t.titulo.trim() === "") lanzarValidacion("El título no puede estar vacío");
  if (t.horas < 0)            lanzarValidacion("Las horas no pueden ser negativas");
}

function lanzarValidacion(msg: string): never {
  throw new Error(`Validación fallida: ${msg}`);
}

const tareas: Tarea[] = [
  { id: 1, titulo: "Diseñar API",      prioridad: "alta",  horas: 8 },
  { id: 2, titulo: "Escribir pruebas", prioridad: "media", horas: 4 },
  { id: 3, titulo: "Actualizar docs",  prioridad: "baja",  horas: 2 },
  { id: 4, titulo: "Code review",      prioridad: "alta",  horas: 3 },
];

const acum = crearAcumulador();
tareas.forEach((t) => {
  validarTarea(t);
  acum.agregar(t.horas);
});

generarReporte(tareas, formatearTarea);
console.log(`Horas totales (closure): ${acum.obtener()}h`);
const alta = buscarTarea("alta");   
const t1   = buscarTarea(1);        

console.log("Tareas de alta prioridad:", alta.map((t) => t.titulo));
console.log("Tarea #1:", t1?.titulo);