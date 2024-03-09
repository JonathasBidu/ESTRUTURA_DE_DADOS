# 4. Construa um programa em Python que
# (a) Crie diversos nós, utilizando os construtores de dicionário vistos na aula;
# (b) Aplique as funções de manipulaçãoo de dicionários vistas em aula nos nós,
# mostrando em tela os resultados;

# classe com a estrtura de nó que fará parte da resolução do exercício
class Node():
    def __init__(self, chave: int)->None:
        self.chave = chave
        self.prox = None

# classe Lista de nós que atuará em conjunto com a classe nó na resolução do exercício
class ListaEncadeada():

    # iniciando a estrutura da lista com 2 atributos nó cabeça e o tamanho da lista
    def __init__(self)->None:
        self.head = None
        self.size = 0

    # método para adicionar um novo nó na lista
    def append(self, chave: int)->None:
        # inserção quando a lista já possui elementos
        if self.head:
            # fazendo uso de um ponteiro que começa apontando para o nó cabeça
            ptr = self.head
            # verificando se o ponteiro é None, caso seja, entrará no loop
            while(ptr.prox):
                # enquanto o ponteiro não estiver apontando para None o loop avança
                # fazendo o ponteiro apontar para o próximo até que chegue no último elemento 
                # e esse estará apontando para None  
                ptr = ptr.prox
            # criando um novo nó e associando ao último ponteiro o qual está apontando
            # nulo
            ptr.prox = Node(chave) 
        else:
            # primeira inserção na lista, caso a lista esteja vazia
            self.head = Node(chave)
        # toda vez que é inclementado uma chave na lista de nó a lista aumenta seu
        # tamanho em um elemento
        self.size += 1
        
    # Método que retorna o tamanho da lista de nós e associa um índice ao nó em questão         
    def __len__(self)->None:
        return self.size
    
    def get(self, indice: int):
        ...       
    
    def set(self, indce: int, chave: int):
        ...

    # método para recuperar o valor da chave do índice desejado
    def __getitem__(self, indice: int)->None:
        # usando um ponteiro que aponta para o primeiro nó da lista
        ptr = self.head
        # iterando na lista até o índice desejado
        for i in range(indice):
            # verificando se a lista não está vazia
            if ptr:
                # fazendo o ponteiro avançar até que o próximo seja None
                ptr = ptr.prox
            # se a lista estiver vazia essa condição lançará um erro pois,
            # o usuário estará tentando acessar um elemento que não existe
            else:
                raise IndexError ("list index out of range")
        # verificando se o ponteiro não está no None
        # caso não não esteja retorna o valor da chave está apontado
        if ptr:
            return ptr.chave
        # caso esteja apontado para None novamente o erro será mostrado
        raise IndexError ("list index out of range")
        
    # método para modificar o valor da chave associada ao um índice informado pelo usário
    def __setitem__(self, indice: int, chave: int)->None:
        # usando um ponteiro que aponta para o primeiro nó da lista
        ptr = self.head
        # iterando na lista até o índice do nó desejado
        for i in range(indice):
            # verificando se a lista não está vazia
            if ptr:
                # fazendo o ponteiro avançar até que o próximo seja None
                ptr = ptr.prox
            # se a lista estiver vazia essa condição lançará um erro pois
            # o usuário estará tentando modificar um elemento que não existe
            else:
                raise IndexError ("list index out of range")
        # verificando se o ponteiro não está no None
        # caso não não esteja modifica o valor da chave que o ponteiro está apontado
        if ptr:
            ptr.chave = chave
        # caso esteja apontado para None novamente o erro será mostrado
        else:
            raise IndexError ("list index out of range")
    
    # método que retorna o índice da chave digitada pelo usuário 
    def index(self, chave: int)->int:
        ptr = self.head
        i = 0
        # pecorre a lista enquanto o ponteiro não estiver apontando para None
        while ptr:
            if ptr.chave == chave:
                return i
            ptr = ptr.prox
            i += 1
        # caso o laço acima não encotre o valor da chave, quer dizer que ela não está na lista
        # dessa forma, um erro será gerado
        raise ValueError (f"{chave} is not in list")
    # método para retornar o objeto em forma de lista
    def __repr__(self):
        r = ''
        ptr = self.head
        while ptr:
            r = r + str(ptr.chave) + ' '
            ptr = ptr.prox
        return '[ ' + r + ']'
    # Método para deletar todos os nós da lista
    def clear(self):
        # Usando um ponteiro que começa apontando para o nó cabeça
        ptr = self.head
        while ptr:
            # Armazenando a referência para o próximo nó
            proximo = ptr.prox
            # Removendo o nó atual, cortando a referência
            del ptr
            # Movendo o ponteiro para o próximo nó
            ptr = proximo
        # Atualizando o atributo size para 0, pois a lista ficou vazia
        self.size = 0
        # Definindo o nó cabeça como None para indicar que a lista está vazia
        self.head = None
   

lista1 = ListaEncadeada()
lista1.append(9)        
lista1.append(55)        
lista1.append(2)        
print(f"A lista 1 é {lista1}")       
print(f'O tamanho da lista é: {len(lista1)}\n')
novalista = ListaEncadeada()
novalista.append(9)        
novalista.append(55)        
novalista.append(2)        
novalista.append(6)        
novalista.append(0)        
novalista.append(102)        
novalista.append(3)        
novalista.append(67)        
novalista.append(78) 
print(f"A nova lista é {novalista}")       
print(f'O tamanho da nova lista é: {len(novalista)}\n')
# imprimindo o valor das chaves dos índices desejado 
print(f"O valor da chave do nó de índice {1} é: {lista1[1]}")
print(f"O valor da chave do nó de índice {2} é: {lista1[2]}")
print(f"O valor da chave do nó de índice {0} é: {lista1[0]}")
# retornando o índice da chave desejada, caso o usuário digite uma chave 
# que não esteja na lista ele retornará um value error
print(f"O elemento {9} está associado ao índice {lista1.index(9)}")
print(f"O elemento {2} está associado ao índice {lista1.index(2)}\n")
# Deletando todos os nós da lista1 antes de deletar a lista por completo
lista1.clear()
print(f"A lista 1 após deletar todos os nós é {lista1}")
print(f'O tamanho da lista é: {len(lista1)}\n')



