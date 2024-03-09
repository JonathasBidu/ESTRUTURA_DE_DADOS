import time

from random import randint

# função para preencher um vetor qualquer de tamanho n
def preenche(n: int)->list:
    vet = []
    for i in range(n):
        vet.append(randint(0,100))
    return vet

# função decoradora para realizar o cálculo do tempo gasto pelo programa
def temp_insert(finsert_sort):
    def wrapper(vet: list)->list:
        n = len(vet)
        begin = time.time()
        finsert_sort(vet)
        end = time.time()
        print(f"O tempo de execução é {end - begin:.4f} segundos para um vetor de tamanho {n}")
    return wrapper

# função inserção ordenada
@temp_insert
def insertion_sort(lista: list)->list:
    n = len(lista)
    # varre o vetor a partir do segundo elemento
    for i in range(1, n):
        elemento = lista[i]
        j = i - 1
        # compara se o elemento da posição anterior é maior que o próximo
        while j >= 0 and lista[j] > elemento:
            # troca com elemento anterior com sucessor
            lista[j+1] = lista[j]
            # evita o loop infinito
            j -= 1
        lista[j+1] = elemento
    return lista

n = int(input("digite o tamanho do vetor: "))
lista = preenche(n)
ins = insertion_sort(lista)
# end = time.time()
# print(f"Tempo gasto pelo programa para ordenar um vetor de tamanho {n} é {end - begin:.4f}")




    

