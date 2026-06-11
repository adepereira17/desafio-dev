def eh_palindromo(numero:int) -> bool:
    numero_original = numero
    invertido = 0

    while numero > 0:
        digito = numero % 10
        invertido = (invertido * 10) + digito
        numero = numero // 10

    return numero_original == invertido

## Casos de teste
if __name__ == "__main__":
    print(f"121 é palíndromo? {eh_palindromo(121)}")
    print(f"4554 é palíndromo? {eh_palindromo(4554)}")
    print(f"123 é palíndromo? {eh_palindromo(123)}")
    print(f"7 é palíndromo? {eh_palindromo(7)}")
