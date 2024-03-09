# 2. Implementar em linguagem Python, a representação de um nó. Os membros do
# dicionário são
# • chave: dado do tipo int;
# • prox: referência para um dado do tipo no;


# Objeto nó proposto no exercício criado pelo classe Node (nó em portugês)
class Node:
    def __init__(self, chave: int) -> None:
       self.chave = chave
       self.prox = None
    
# criando um nó
no1 = Node(5)
print(f"O valor da chave do no1 é: {no1.chave} \nEstá apontado para: {no1.prox}")
# criando um segundo nó
no2 = Node(87)
# apontando nó 2 para nó 1
no1.prox = no2
print(f"O valor da chave do no2 é: {no2.chave} \nEstá apontado para: {no1.prox}")
# Exibindo o valor da chave para onde o no1 está apontando
print(f"O valor da chave para onde o nó 1 está apontando é: {no1.prox.chave}")

