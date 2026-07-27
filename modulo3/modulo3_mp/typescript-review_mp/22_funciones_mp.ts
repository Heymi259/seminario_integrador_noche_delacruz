function calcularDescuento(precio: number, porcentaje: number): number {
  const descuento = precio * (porcentaje / 100);
  return Number((precio - descuento).toFixed(2));
}

function resumenCompra(producto: string, precio: number, descuento: number): string {
  const final = calcularDescuento(precio, descuento);
  return `${producto}: $${precio} → $${final} (${descuento}% off)`;
}

console.log(resumenCompra("Teclado", 120, 15));  
console.log(resumenCompra("Monitor", 350, 20));  
console.log(resumenCompra("Mouse", 45, 0));      