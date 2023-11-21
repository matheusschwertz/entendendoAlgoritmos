# Ordenação por Seleção

A ordenação por seleção é um algoritmo simples e intuitivo de ordenação que consiste em iterativamente encontrar o menor (ou maior) elemento de uma lista não ordenada e trocá-lo com o primeiro elemento não ordenado. Esse processo é repetido até que toda a lista esteja ordenada.

## Complexidade
A ordenação por seleção possui uma complexidade de tempo de \(O(n^2)\) no pior caso, tornando-se menos eficiente para grandes conjuntos de dados.

## Funcionamento

1. **Encontrar o Menor Elemento:**
   - Inicializa uma variável para armazenar o menor elemento e seu índice.
   - Itera pela lista para encontrar o menor elemento.
   - Atualiza a variável com o menor elemento e seu índice.

2. **Trocar Elementos:**
   - Troca o menor elemento encontrado com o primeiro elemento não ordenado na lista.

3. **Repetição:**
   - Repete os passos 1 e 2 para o restante da lista não ordenada.

4. **Conclusão:**
   - Ao final do processo, a lista estará ordenada.

## Implementação Python

```python
def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i 

    return menor_indice

def ordenacaoPorSelecao(arr):
    for i in range(len(arr)):
        # Encontra o menor elemento na lista não ordenada
        menor_indice = buscaMenor(arr[i:])
        
        # Troca o menor elemento com o primeiro elemento não ordenado
        arr[i], arr[i + menor_indice] = arr[i + menor_indice], arr[i]

# Exemplo de Uso
minha_lista = [64, 25, 12, 22, 11]
ordenacaoPorSelecao(minha_lista)
print("Lista Ordenada:", minha_lista)

