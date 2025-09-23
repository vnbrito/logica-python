import os
os.system('cls')

soma = 0
n = 1

#while n <= 10:
#    soma = soma + n
#    n = n + 1
#       print(f'Soma: {soma}') - Apenas para visualização do que está acontencendo.
#       print(f'n: {n}')

for index in range(1,11):
    soma = soma + n
    n = 1

#Uma forma mais enxuta seria:
for index in range(1,11):
    soma = soma + index

#Mais enxuto ainda:
for index in range(1,11):
    soma += index

#Para diversão, uma maneira de deixar ainda mais enxuto
soma = sum([i for i in range(1,11)])

print(f'A soma dos números de 1 a 10 é {soma}')

