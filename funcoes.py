# f(x) = y
# f(x, y ,z)
# f(x) = 2x 
# f(2) = 4
# f(5) = 10
import os
os.system('cls')

def olaMundo():
    print('Olá, mundo!')

olaMundo()
olaMundo()
olaMundo()
olaMundo()

def olaPessoa(nome):
    print(f'Olá, {nome}!')

olaPessoa('Andre')
olaPessoa('Joaquina')
olaPessoa('Enzo')
olaPessoa('João')
olaPessoa('Valentina')

def dobro(numero):
    return numero * 2

print(dobro(5))

#-------------------------------------------------------#
def dobro(numero):
    return numero * 2

print(dobro(5) + 2)
#-------------------------------------------------------#

def multiplicaDoisNumeros(a, b):
    return a * b

print(multiplicaDoisNumeros(3,6))
print(multiplicaDoisNumeros(3)) #Nesse caso vai apresentar erro pois o programa obriga a inserir dois valores, que foi o definido na função.

#Porém, contudo, todavia, se eu quiser mesmo assim apresentar apenas um valor, com o objetivo de o programa o multiplicar por 2, ficará desse jeito:

def multiplicaDoisNumeros(a, b = 2): #Não quer dizer que b vale 2, quer dizer que se b não receber nada, ele vai valer 2. Não é possível fazer o inverso, ou defino os 2 com 2, ou apenas o b.
    return a * b

print(multiplicaDoisNumeros(3))

#-----------------------------------------------------#

x = 5
def soma():
    x = 10 # Variável local
    print(x)
    return x + 1
soma()
print(x)
"""Tomar cuidado com definição de variáveis globais
dentro de função e fora, pois dentro da função ela tem o valor definido apenas lá dentro (Variável Local), se definir fora da função, ela tem aquele valor."""

#-----------------------------------------------------#