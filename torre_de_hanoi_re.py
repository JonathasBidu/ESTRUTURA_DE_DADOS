# Procedimento moverDisco(de, para)
#     Imprimir "Mover disco de", de, "para", para

# Procedimento resolverTorre(n, origem, destino, auxiliar)
#     Se n == 1 Então
#         moverDisco(origem, destino)
#     Senão
#         resolverTorre(n-1, origem, auxiliar, destino)
#         moverDisco(origem, destino)
#         resolverTorre(n-1, auxiliar, destino, origem)

# Função principal:
#     Definir n como o número de discos
#     Definir origem, destino e auxiliar como os nomes das torres

#     resolverTorre(n, origem, destino, auxiliar)
def moverDisco(de, para):
    print("Mover disco de", de, "para", para)

def resolverTorre(n, origem, destino, auxiliar):
    if n == 1:
        moverDisco(origem, destino)
    else:
        resolverTorre(n-1, origem, auxiliar, destino)
        moverDisco(origem, destino)
        resolverTorre(n-1, auxiliar, destino, origem)
    
def main():
    n = int(input("Digite o número de discos: "))
    origem = input("Digite o nome da torre de origem: ")
    destino = input("Digite o nome da torre de destino: ")
    auxiliar = input("Digite o nome da torre auxiliar: ")

    resolverTorre(n, origem, destino, auxiliar)

main()
