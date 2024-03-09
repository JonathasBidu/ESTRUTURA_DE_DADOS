# 4. Uma em C++ e outra em Python em que serão feitos tantos sorteios quanto
# necessário, até que o parâmetro β seja inferior a uma tolerâncias β∗ , definida(lida
# da tela) pelo usuário no início do processo. O vetor deve ser uma lista dinâmica
# - utilizar o container list do Python e o container std::vector, da classe
# <vector> no C++;

# importação de bibliotecas que serão utilizadas ao longo do programa
import random
import math

def D(x):
    P = 0.05*x**3
    return P

# entrada digitada pelo usuário que será usada para limitar as iterações 
beta_u = float(input("Digite uma tolerância mínima menor que (1) e maior que (0.0005) para o parâmetro beta: "))

# atribuição de valores as variáveis que serão utilizadas no decorrer do programa
Nmax = 1000000
soma = 0
soma_2 = 0
N = 0 
lista = []
i = 0 

# condição para que seja possível obter algum cálculo do parâmetro beta nessa simulação
if beta_u > 0.0005 and beta_u < 1:
    # laço que fará a quantidade de iterações enquanto o beta* for menor e com um mínimo de 100 iterações ou máximo de 1 milhão
    while Nmax > 0:
        N += 1 # acumulador que será utilizado na contagem das iterações e será utilizados também nos cálculos a seguir
        x = random.uniform(7, 14) # atribuição de valores das amostras aleatórias
        lista.append(D(x))
        soma += lista[i] # somatório da função de desempenho
        l = soma/N # E(x) valor esperado da simulação
        soma_2 += (lista[i] - l)**2 # somatório da variância 
        v = soma_2 / N # cálculo da variância
        Dp = math.sqrt(v) # cálculo do desvio padrão
        beta = Dp/l 
        beta = beta/math.sqrt(N) # cálculo do parâmetro beta 
        # condição de parada do loop caso beta calculado no loop seja inferior ao estipulado pelo usuário e com o mínimo de 100 iterações
        if N > 100 and beta < beta_u:
            break
        # decremento do número máximo de iterações caso beta não seja inferior ao estipulado pelo usuário
        Nmax -= 1
        i += 1
    
    lista.clear()    
    # saídas esperadas
    print(f"O valor esperado para essa simulação é {l:.4f}")
    print(f"O desvio padrão é {Dp:.4f}")
    print(f"O parâmetro beta para essa simulação é {beta:.6f}")
    print(f"Foram necessárias {N} iterações")
# condição caso o usuário entre com um valor que não faça sentido para o cálculo do beta
else:
    print("O parâmetro tem que ser um valor menor (1) que e maior que (0.0005).")

