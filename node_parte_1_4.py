# # 4. Construa um programa em Python que
# (a) Crie diversos nós, utilizando os construtores de dicionário vistos na aula;
# (b) Aplique as funções de manipulação de dicionários vistas em aula nos nós,

# classe de nó em forma de dicionário de acordo com o modelo proposto pelo exercício acima
class No(dict):
    def __init__(self)->dict:
        self.lista = dict(chave = None, prox = None)
    def __repr__(self) -> str:
        return repr(self.lista)
    # métodos para inserir novos nós a partir de valores de chaves digitadas pelo usuário
    def add(self, chave):
        novo_no = No()
        novo_no.lista["chave"] = chave
        novo_no.lista["prox"] = self.lista["prox"]
        self.lista['prox'] = novo_no.lista
    # método para remover nós a partir da chave digitada pelo usuário
    def remove(self, chave):
        ant = self.lista
        atual = self.lista['prox']
        while atual is not None:
            if atual['chave'] == chave:
                ant['prox'] = atual['prox']
                break
            ant = atual
            atual = atual['prox']
    # método para recupere apenas os valores das chaves em formato de vetor
    def valor_chave(self):
        valor = []
        ptr = self.lista['prox']
        while ptr is not None:
            valor.append(ptr["chave"])
            ptr = ptr['prox']
        return valor

# Demostração dos resultados dos nós na tela
dic = No()
print(dic)
valores = dic.valor_chave()
print("Valores das chaves:", valores)
dic.add(5)
dic.add(44)
dic.add(9)
print(dic)
valores = dic.valor_chave()
print("Valores das chaves:", valores)
dic.remove(5)
print(dic)
valores = dic.valor_chave()
print("Valores das chaves:", valores)



