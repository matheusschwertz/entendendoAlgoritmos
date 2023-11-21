# Defina a função de buscaMenor
def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i 

    return menor_indice

# Teste a função com uma lista
minha_lista = [5, 2, 8, 1, 6]
indice_do_menor = buscaMenor(minha_lista)

# Imprima o resultado
print(f"O menor elemento está no índice {indice_do_menor} e possui o valor {minha_lista[indice_do_menor]}.")
