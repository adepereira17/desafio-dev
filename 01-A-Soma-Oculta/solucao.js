function somarDigitos(numero){
    let soma = 0;
    while (numero > 0){
        soma += numero % 10;
        numero = Math.floor(numero / 10);
    }

    return soma;
}

//Casos de testes para validação dos alunos
console.log(`Resultado para 527: ${somarDigitos(527)}`);
console.log(`Resultado para 109: ${somarDigitos(103)}`);
console.log(`Resultado para 9: ${somarDigitos(9)}`);
