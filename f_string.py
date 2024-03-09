from random import randint

def vetor(n):
    vet = []
    for i in range(n):
        vet.append(randint(-1,1))
    return vet


vet = vetor(10)
cont_1 = 0
cont_2 = 0
cont_3 = 0

print()

for i in range(len(vet)):
    if vet[i] > 0:
        cont_1 += 1
    elif vet[i] == 0:
        cont_3 += 1
    else:
        cont_2 += 1

print(vet)
print(f"A quantidade de números positivos são {cont_1}, de negativos são {cont_2} e de zero é {cont_3}")