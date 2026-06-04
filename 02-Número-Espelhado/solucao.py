def inverter_numero(numero: int) -> int:
    invertido = 0
    while numero > 0:
        digito = numero % 10;
        invertido = (invertido * 10) + digito
        numero = numero // 10
    return invertido

## Casos de teste
if __name__ == "__main__":
    print(f"Invertido 3815: {inverter_numero(3815)}")
    print(f"Invertido 100: {inverter_numero(100)}")
    print(f"Invertido 7: {inverter_numero(7)}")
    
