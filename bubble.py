from random import randint
import time

# função para preencher um vetor qualquer de tamanho n
def preenche(n: int)->list:
    vet = []
    for i in range(n):
        vet.append(randint(0,100))
    return vet

# função decoradora com cálculo de tempo
def temp_bubble(fbubble):
    def wrapper(vet: list)->list:
        n = len(vet)
        begin = time.time()
        fbubble(vet)
        end = time.time()
        print(f"O tempo de execução é {end - begin:.4f} segundos para um vetor de tamnho {n}")
    return wrapper

# função de ordenação bolha
@temp_bubble
def bubble_sort(lista):
    # tamanho da lista
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            # lógica de comparação caso o elemento da posição seja maior que o sucessor ele troca de posição
            if lista[j] > lista[j+1]:
                # trocas de posição caso for verdade
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

# testes
n = int(input("digite o tamanho do vetor: "))
lista = preenche(n)
print(lista)
bub = bubble_sort(lista)
print(lista)


