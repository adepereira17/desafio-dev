# DesafioDev 03: o número é palíndromo?

## Enunciado
Crie um algoritmo que determine se um número inteiro positivo é um palíndromo. Um número é palíndromo quando lido da esquerda para a direita ou da direita para a esquerda resulta no mesmo valor.

* **Exemplos:**
* `121` → `verdadeiro`
* `4554` → `verdadeiro`
* `123` → `falso`

### Regra crítica
* **Não é permitido** converter o número para string em nenhum momento da resolução.

## Lógica de resolução
Este desafio utiliza exatamente a mesma lógica matemática do **Desafio 02 (Número Espelhado)**, mas com um detalhe crucial no final:
1. Guardamos uma cópia do número original em uma variável auxiliar (exemplo: `numero_original`), pois o número principal será reduzido a `0` dentro do laço `while`.
2. Invertemos o número usando operações matemáticas (`% 10` e `* 10`).
3. No final, comparamos: se o `numero_original` for igual ao número `invertido`, ele é um palíndromo (retorna verdadeiro). Caso contrário, não é (retorna falso).
