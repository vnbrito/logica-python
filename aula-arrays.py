import os
os.system('cls')

#Arrays são estruturas de dados que permitem guardar dados dentro de uma única variável.

x = [1, 2, 3]
x[0] = 25
#Saída = [25, 2, 3]
#Sintaxes do array: 
#x.append() = adicionar no final;
#x.sort() = ordenar;
#x.reverse() = inverter a ordem;
#x.pop() = remove do final;
#x.insert(1, 55) = adiciona o valor no array "empurrando os outros pra frente";
#-------------------------------------------------------#
#x.insert (3, [1,2,3]), ou seja, é possível adicionar lista dentro de lista;

notas = [9, 9.5, 10, 9.8]

media = 0
for nota in notas:
    media += nota

media /= 4

print(f'A média é {media}')