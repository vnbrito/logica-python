import os
os.system('cls')

print('Olá, eu sou a sua assistente, Pythrina. O que você quer fazer hoje?')

comando = input('Digite um comando: ')

match comando: 
    case 'oi' | 'olá' | 'Hello':
        print('Oi, como vai você?')
    case 'tchau' | 'bye' | 'fim' | 'até mais':
        print('Tchau, foi bom conversar com você!')
    case 'piada' | 'joke':
        print('Sabe qual é o padroeiro das pessoas que trabalham com TI? O São Login')
    case 'clima' | 'previsão do tempo':
        print('Tá muuuuuuuuuito quente!! Deve ter passado de 40ºC!')
    case _:
        print('Desculpe, não entendi o comando.')
