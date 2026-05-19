def somar_digitos(numero:int) -> int:
    soma = 0
    while numero > 0:
        soma += numero % 10
        numero = numero // 10
    return soma

## Casos de testes para validação dos alunos
if __name__ == "__main__":
    print(f"Resultado para 527: {somar_digitos(527)}")
    print(f"Resultado para 103: {somar_digitos(103)}")
    print(f"Resultado para 9: {somar_digitos(9)}")


