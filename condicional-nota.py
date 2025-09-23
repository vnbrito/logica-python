import os
os.system('cls')

print('Vamos descobrir se você passou de ano ou se ficou de recuperação?')

nota = int(input('Digite sua nota: '))

if nota >= 7:
    print('Passou!')
else:
    if nota < 5:
        print('Não passou!')
    else:
        print('Recuperação!')
#----------------------------------------------------------------------------------------------#
#Há uma maneira de deixar o código enxuto, que seria:

nota = int(input('Digite sua nota: '))

if nota >= 7:
   print('Passou!!!!')
elif nota <5:
    print('Não passou! :(')
else:
    print('Recuperação! Boa-Sorte!')