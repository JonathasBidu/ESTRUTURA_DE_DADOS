from random import randint
import time

# função para preencher um vetor qualquer de tamanho n
def preenche(n: int)->list:
    vet = []
    for i in range(n):
        vet.append(randint(0,100))
    return vet

# função decoradora para realizar o cálculo do tempo gasto pelo programa
def temp_selection(fselection):
    def wrapper(vet: list)->list:
        n = len(vet)
        begin = time.time()
        fselection(vet)
        end = time.time()
        print(f"O tempo de execução é {end - begin:.4f} segundos para um vetor de tamanho {n}")
    return wrapper

# função de ordenação por seleção 
@temp_selection
def selection_sort(lista: list)->list:
    n = len(lista)
    # varre o vetor até o penúltimo elemento
    for i in range(n-1):
        # inicia o mínimo na primeira posição de vetor
        min_index = i
        # varre a sub-lista de 0 até n-1
        for j in range(i, n):
            # encontra o menor valor dentro da lista
            if lista[j] < lista[min_index]:
                # posiciona o índice mínimo no menor valor encontrado
                min_index = j
        # compara se o valor na posição i é maior que o valor mínimo 
        if lista[i] > lista[min_index]:
            # variável auxiliar para guardar um dos extremos
            aux = lista[i]
            # troca do maior com o menor
            lista[i] = lista[min_index]
            lista[min_index] = aux
    return lista



# diversos testes para provar a certeza de que a lógica está correta
n = int(input("digite o tamanho do vetor: "))
lista = preenche(n)
sel = selection_sort(lista)


