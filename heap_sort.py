import random
import time

# Funçao para preencher um vetor qualquer de tamanho n
def preenche(n: int)->list:
    vet = []
    for i in range(n):
        vet.append(random.randint(0, 100))
    return vet

def temp_heap(fheapsort):
    def wrapper(vet: list)->list:
        n = len(vet)
        begin = time.time()
        fheapsort(vet)
        end = time.time()
        print(f"O tempo de execução é {end - begin:.8f} segundos para um vetor de tamnho {n}")
    return wrapper

# Função para ajustar o heap a partir do índice i
def  ajustar_heap(vet, n, i):
    maior = i
    esq = 2*i+1
    dir = 2*i+2

    # verifica se o filho da esquerda é maior que o maior a raíz
    if esq < n and vet[i] < vet[esq]:
        maior = esq

    # verifca se o filho da direita é maior que o maior atual
    if dir < n and vet[maior] < vet[dir]: 
        maior = dir
    
    #  se o maior não for a raíz, faz a troca e ajusta o heap recursivamente
    if maior != i:
        aux = vet[i]
        vet[i] = vet[maior]
        vet[maior] = aux
        ajustar_heap(vet, n, maior)

    # Função para realizar o Heap Sort em um vetor qualquer
@temp_heap
def heapsort(vet):
    n = len(vet)

    # constroi um heap máximo a partir dos elementos que não são folhas
    # (n//2-1) até a raíz (0)
    for i in range(n//2-1, -1, -1):
        ajustar_heap(vet, n, i)

    # extrai elementos um por um do heap
    for i in range(n-1, 0, -1):
        # move o elemnto raíz (maior elemento) para o final
        aux = vet[i]
        vet[i] = vet[0]
        vet[0] = aux
        # ajusta o heap com o novo tamanho reduzido
        ajustar_heap(vet, i, 0)

n = int(input("Informe o tamnho do vetor: "))
vetor = preenche(n)
heap = heapsort(vetor)
