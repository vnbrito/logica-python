import os
os.system('cls')

#Meu crachá de programador!
dados = []

nome = input('Digite o seu nome: ')
dados.append(nome)
idade = int(input('Digite a sua idade: '))
dados.append(idade)
lingFavorita = input('Digite a sua linguagem favorita: ')
dados.append(lingFavorita)
emoji = input('Qual seu emoji favorito?: ')
dados.append(emoji)


print('-' * 20)
print()
print('*Crachá do Dev*')
print(dados[0])
print(dados[1])
print(dados[2])
print(dados[3])
print()
print('-' * 20)
