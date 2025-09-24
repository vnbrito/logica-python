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

os.system('cls')

print('-' * 25)
print()
print('*Crachá do Dev*')
print()
print(f'Nome: {dados[0]}')
print(f'Idade: {dados[1]}','anos')
print(f'Linguagem Favorita: {dados[2]}')
print(f'Emoji Preferido: {dados[3]}')
print()
print('-' * 25)
print()

