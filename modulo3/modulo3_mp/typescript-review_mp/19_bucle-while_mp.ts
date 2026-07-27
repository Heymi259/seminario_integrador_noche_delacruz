// bucle-while.ts


let contador: number = 1;
while (contador <= 5) {
  console.log(`Contador: ${contador}`);
  contador++;
}


let numero: number = 10;
do {
  console.log(`Número: ${numero}`);
  numero -= 3;
} while (numero > 0);


function simularAdivinanza(): void {
  const secreto: number = Math.floor(Math.random() * 10) + 1;
  const intentos: number[] = [3, 7, 5, secreto]; // simulamos intentos
  let intentoActual: number = 0;
  let acertado: boolean = false;

  while (intentoActual < intentos.length && !acertado) {
    const intento: number = intentos[intentoActual];
    intentoActual++;

    if (intento === secreto) {
      console.log(`¡Acertaste! El número era ${secreto} (intento ${intentoActual})`);
      acertado = true;
    } else if (intento < secreto) {
      console.log(`${intento} → Demasiado bajo`);
    } else {
      console.log(`${intento} → Demasiado alto`);
    }
  }
}

simularAdivinanza();