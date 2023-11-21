def fatorial(n):
    # Caso base: fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    else:
        # Chamada recursiva: n! = n * (n-1)!
        return n * fatorial(n - 1)

# Teste
numero = 5
resultado = fatorial(numero)
print(f'O fatorial de {numero} é {resultado}')
