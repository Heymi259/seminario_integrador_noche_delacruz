// Concepto puro


type Transformador = (x: number) => number;
type Predicado     = (x: number) => boolean;

function aplicar(n: number, fn: Transformador): number {
  return fn(n);
}

function multiplicadorDe(factor: number): Transformador {
  return (x) => x * factor;
}
const triple = multiplicadorDe(3);
const cuadrado: Transformador = (x) => x * x;

console.log(aplicar(5, triple));    
console.log(aplicar(5, cuadrado)); 
console.log(aplicar(5, (x) => x + 10));


function filtrar(nums: number[], condicion: Predicado): number[] {
  return nums.filter(condicion);
}

const nums = [1, 2, 3, 4, 5, 6, 7, 8];
console.log(filtrar(nums, (n) => n % 2 === 0)); 
console.log(filtrar(nums, (n) => n > 5));       


