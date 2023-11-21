# Busca Binária

A busca binária é um algoritmo eficiente para encontrar um elemento específico em uma lista ordenada. Aqui está um breve resumo do processo:

1. **Ordenação:** A lista em que você está procurando deve estar ordenada, o que significa que os elementos estão dispostos em ordem crescente ou decrescente.

2. **Início e Fim:** Defina dois índices, geralmente chamados de `baixo` e `alto`, inicialmente apontando para o início e o final da lista, respectivamente.

3. **Meio da Lista:** Calcule o índice do meio da lista usando a fórmula `(baixo + alto) // 2`.

4. **Comparação:**
   - Se os elementos forem iguais, você encontrou o elemento e retorna o índice.
   - Se o elemento no meio for maior que o elemento procurado, ajuste o índice `alto` para `meio - 1`, restringindo a busca à metade inferior da lista.
   - Se o elemento no meio for menor que o elemento procurado, ajuste o índice `baixo` para `meio + 1`, restringindo a busca à metade superior da lista.

5. **Iteração:** Repita os passos 3 e 4 até que o elemento seja encontrado ou até que `baixo` seja maior que `alto`. Se `baixo` for maior que `alto`, o elemento não está na lista.

A busca binária tem uma complexidade de tempo de O(log n), o que a torna significativamente mais rápida do que buscas lineares, especialmente em listas grandes. É um algoritmo eficaz para encontrar elementos em listas ordenadas.
