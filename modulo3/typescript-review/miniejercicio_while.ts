let conteoTiradas = 0;
let resultado = 0;

while (resultado !== 6) {
  resultado = Math.floor(Math.random() * 6) + 1;
  conteoTiradas += 1;
}

console.log(`Se necesitaron ${conteoTiradas} tiradas para sacar un 6.`);
