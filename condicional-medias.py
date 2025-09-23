import os
os.system('cls')

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media > 5:
    print('Você passou!')
    print(media)
else:
    print('Sua média é: ', media)
    print('Você reprovou, deve realizar a recuperação!')
    print('Boa Sorte!')
    
