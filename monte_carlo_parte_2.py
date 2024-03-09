"""2. Faça um programa que realize tantos sorteios quanto necessário, até que o parâmetro
β seja inferior a uma tolerâncias β∗, definida(lida da tela) pelo usuário no início do processo. """

# importação de bibliotecas que serão utilizadas ao longo do programa
import random
import math
# função de distribuição uniforme dado um intervalo (a, b)
def f(a,b):
    x = random.uniform(a, b)
    return x
# função de desempenho 
def D(x):
    # função teste podendo ser utilizada outra se for o caso
    pot = 0.05*(x**3)
    return pot
# entrada digitada pelo usuário que será usada para limitar as iterações 
beta_u = float(input("Digite uma tolerância mínima menor que zero para o parâmetro beta: "))
beta = 0
n = 0
soma = 0
soma2 = 0

if beta_u > 0 and beta_u < 1:
    while beta < beta_u:
        n+=1
        x = f(7.0, 14.0)        
        d = D(x)
        soma += d
        mu = soma/(n)
        soma2 += (d-mu)**2
        v = soma2/(n)
        s = math.sqrt(v)
        beta = s/(mu*(math.sqrt(n)))
        if n+1 == 1000000:
            break

    print(f"O valor esperado é {mu}")
    print(f"O variância é {v:.2f}")
    print(f"O desvio padrão é {s:.2f}")
    print(f"O erro é {beta:.5f}")
    print(f"Foram feitos {n} sorteios")
else:
    print("Intervalo não válido!")