import os
os.system('cls')

tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

"""
forma avançada e resumida de fazer o mesmo que o código acima:
tabuleiro = [ [' ' for _ in range(3)] for _ in rage(3) ]
"""
jogador = 'X' # Variável global

def exibeTabuleiro():
    for linha in tabuleiro:
        #print(f'{linha[0]}|{linha[1]}|{linha[2]}')
        print('|'.join(linha))
        #print('-----')
        print('-' * 5)

def jogada(linha, coluna):
    if linha < 0 or linha > 2:
   #outras opções:
   #if not 0 <= linha <= 2: 
   #if (
   #    not 0 <= linha <= 2 or
   #    not 0 <= coluna <= 2 or 
   #    taubleiro[linha][coluna] != ' '
   # ):
        print('Jogada inválida')
        return jogador
    if tabuleiro[linha][coluna] != ' ':
        print('Jogada inválida!')
        return jogador
    #Opção 1: global jogador
    tabuleiro[linha][coluna] = jogador
    #if jogador == 'X':
    #    return 'O'
    #else:
    #    return 'X'
    #
    #Ou podemos fazer assim:
    return 'O' if jogador == 'X' else 'X'
    
while True:
    print(f'Jogador da vez: {jogador}')
    try:
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        jogador = jogada(linha, coluna)
    except (ValueError, IndexError):
        print('Digite valores numéricos entre 0 e 2')
    exibeTabuleiro()
