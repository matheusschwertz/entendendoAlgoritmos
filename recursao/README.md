# Recursão

A recursão é um conceito fundamental na programação, onde uma função chama a si mesma durante a execução. Isso permite a divisão de problemas em subproblemas menores, facilitando a resolução e compreensão.

## Como Funciona

A recursão envolve a divisão de um problema em casos menores e a resolução desses casos. Cada chamada recursiva leva a uma subdivisão do problema até que seja atingido um ponto de parada, conhecido como "caso base".

## Exemplo: Cálculo do Fatorial

O cálculo do fatorial é um exemplo clássico de recursão. A fórmula para o fatorial de um número \(n\) é dada por:

\[ n! = n \times (n-1) \times (n-2) \times \ldots \times 2 \times 1 \]

A função recursiva em Python para calcular o fatorial pode ser assim:

```python
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
```
## Benefícios da Recursão
#### Elegância: A recursão pode levar a soluções elegantes e concisas para problemas complexos.
#### Divisão de Problemas: Permite a divisão de um problema grande em subproblemas menores, facilitando a resolução.

## Conclusão
#### A recursão é uma ferramenta poderosa, mas deve ser usada com sabedoria. Compreender seus princípios fundamentais e aplicá-la corretamente pode levar a soluções claras e elegantes para diversos problemas.