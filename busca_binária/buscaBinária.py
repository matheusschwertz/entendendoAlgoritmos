def pesquisa_binaria(lista, item):
    # Inicializa os índices de busca
    baixo, alto = 0, len(lista) - 1
    
    # Realiza a busca binária
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        # Verifica se o elemento foi encontrado
        if chute == item:
            return meio

        # Ajusta os índices de acordo com a comparação
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    # Retorna None se o elemento não estiver na lista
    return None

# Exemplo de uso
minha_lista = [1, 3, 5, 7, 9]
item_procurado = 9

# Executa a busca binária e imprime o resultado
resultado = pesquisa_binaria(minha_lista, item_procurado)
print(f'O item {item_procurado} está na posição {resultado}.' if resultado is not None else f'O item {item_procurado} não está na lista.')
