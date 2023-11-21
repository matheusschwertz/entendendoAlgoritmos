class Item:
    def __init__(self, tipo):
        self.tipo = tipo

    def e_uma_caixa(self):
        return self.tipo == 'caixa'

    def e_uma_chave(self):
        return self.tipo == 'chave'

class Caixa:
    def __init__(self, itens):
        self.itens = itens

    def crie_uma_pilha_para_busca(self):
        return self.itens

# Função atualizada para retornar um valor
def procure_pela_chave(caixa_principal):
    pilha = [caixa_principal]

    while pilha:
        caixa = pilha.pop()

        for item in caixa.itens:
            if isinstance(item, Item):
                if item.e_uma_caixa():
                    pilha.append(item)
                elif item.e_uma_chave():
                    return True  # Retorna True se a chave for encontrada

    return False  # Retorna False se a chave não for encontrada

# Teste
item_chave = Item('chave')
caixa_interna = Caixa([item_chave, Item('livro'), Item('caneta')])
caixa_principal = Caixa([caixa_interna, Item('outro_item')])

encontrou_chave = procure_pela_chave(caixa_principal)

if encontrou_chave:
    print("A chave foi encontrada!")
else:
    print("A chave não foi encontrada.")
