# DesafioDev 01: A Soma Oculta

## Enunciado
Dado um número inteiro positivo, calcule a soma de todos os seus dígitos.

* **Entrada:** 527
* **Saída:** 14 (pois 5 + 2 + 7 = 14)

### Regra Crítica
* **Não é permitido** converter o número para string em nenhum momento da resolução.

---

## Lógica de Resolução
Para resolver este problema sem transformar o número em texto, utilizamos operadores matemáticos (`%` resto da divisão e `//` ou `Math.floor()` para divisão inteira):
1. O resto da divisão por 10 (`numero % 10`) isola o **último dígito** do número.
2. Adicionamos esse dígito à nossa variável soma.
3. Dividimos o número por 10 e pegamos apenas a parte inteira (`numero // 10`), **eliminando** o último dígito que já foi somado.
4. Repetimos o processo até que o número seja `0`.

