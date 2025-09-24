import os
os.system('cls')

print('Olá, seja bem-vindo! Meu nome é Pythrina e serei sua assistente em tempo integral! O que deseja fazer hoje?')

while True:
    comando = input('Digite seu comando: ')
    os.system('cls')
    match comando:
        case 'olá' | 'oi' | 'como vai?':
            print('Olá, como você está?')
        case 'tchau':
            print('Mas já vai? Então tchau!')
        case 'previsão do tempo':
            print('Hoje o tempo está nublado com chance de chuva mais tarde! E muuuuito calor.')
        case 'horas':
            print('Agora são 13:03 no horário de Brasília.')
        case _:
            print('Desculpe, não reconheço esse comando.')
            break
    
        

