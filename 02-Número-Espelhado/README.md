# DesafioDev 02: Número Espelhado

## Enunciado
Crie um algoritmo que recebe um número inteiro positivo e retorne esse número invertido (espelhado).
* **Entrada:** 3815
* **Saída:** 5183

### Regra Crítica:
* **Não é permitido** converter o número para string em nenhum momento da resolução.

---

## Lógica de Resolução
Assim como no desafio 01, usamos a matemática para isolar o último dígito, mas adicionamos um passo para reconstruir o número invertido:
1. Iniciamos uma variável `invertido = 0`.
2. Isolamos o último dígito do número original usando `numero % 10`.
3. Multiplicamos o valor atual de `invertido` por 10 (abrindo espaço para a nova casa decimal) e somamos o dígito isolado.
4. Removemos o último dígito do número original usando divisão inteira (`numero // 10`) ou `Math.floor()`.
5. Repetimos até que o número original chegue a `0`.
