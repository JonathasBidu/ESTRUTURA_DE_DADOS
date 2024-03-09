# 3. Construa em C++ e Python um programa que:
#  (a) crie 3 nós n1, n2 e n3, inicializando os dois  ́ultimos(n2 e n3) com chaves
#  distintas e apontadores nulos;
#  (b) armazene um inteiro em n1;
#  (c) faça n1 apontar para n2, e n2 para n3;
#  (d) imprima para cada nó sua chave e o endereço do nó para o qual aponta no
#  Python, utilizar o comando id(), para retornar o endereço de memória de
#  uma variável;

# Objeto nó proposto no exercício criado pelo classe Node (nó em portugês)
class Node:
    def __init__(self, chave: int) -> None:
       self.chave = chave
       self.prox = None   
# (a) crie 3 nós n1, n2 e n3, inicializando os dois  ́ultimos(n2 e n3) com chaves
no1 = Node(None)
no2 = Node(55)
no3 = Node(78)
# Definindo apontadores nulos
no1.prox = None
no2.prox = None
no3.prox = None
# (b) Armazene um inteiro em no1
no1.chave = 39
# (c) faça n1 apontar para n2, e n2 para n3;
no1.prox = no2
no2.prox = no3
# (d) imprima para cada nó sua chave e o endereço do nó para o qual aponta no
#  Python, utilizar o comando id(), para retornar o endereço de memória de
#  uma variável;
print(f"O valor da chave do no1 é: {no1.chave} Está apontado para: {id(no1.prox)}")
print(f"O valor da chave do no2 é: {no2.chave} Está apontado para: {id(no2.prox)}")
print(f"O valor da chave do no3 é: {no3.chave} Está apontado para: {id(no3.prox)}")