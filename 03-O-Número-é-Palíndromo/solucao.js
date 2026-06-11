function ehPalindromo(numero){
    const numeroOriginal = numero;
    let invertido = 0;

    while(numero > 0){
        let digito = numero % 10;
        invertido = (invertido * 10) + digito;
        numero = Math.floor(numero / 10);
    }

    return numeroOriginal === invertido;
}

//Casos de teste
console.log(ehPalindromo(4554));
console.log(ehPalindromo(123));
