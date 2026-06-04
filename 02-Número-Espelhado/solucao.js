function inverterNumero(numero){
    let invertido = 0;
    while(numero > 0){
        let digito = numero % 10;
        invertido = (invertido * 10) + digito;
        numero = Math.floor(numero / 10);
    }

    return invertido;
}

//Casos de teste
console.log(`Invertido 3815: ${inverterNumero(3815)}`);
console.log(`Invertido 100: ${inverterNumero(100)}`);
console.log(`Invertido 7: ${inverterNumero(7)}`);
