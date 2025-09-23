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

def temGanhador():
    """Verifica as linhas"""
    for linha in range(3):
        if(
            tabuleiro[linha][0] != ' ' and
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            tabuleiro[linha][0] == tabuleiro[linha][2]
        ):
            print(f'{tabuleiro[linha][0]} GANHOU!!!')
            return True
    
    """Verifica as colunas"""
    for coluna in range(3):
        if(
            tabuleiro[0][coluna] != ' ' and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            tabuleiro[0][coluna] == tabuleiro[2][coluna]
        ):
            print(f'{tabuleiro[0][coluna]} GANHOU!!!')
            return True
        
    """ Verifica as diagonais """
    if(
        tabuleiro[1][1] != ' ' and
        (
            (
                tabuleiro[0][0] == tabuleiro[1][1] and
                tabuleiro[0][0] == tabuleiro[2][2]
            )or
            (
                tabuleiro[0][2] == tabuleiro[1][1] and
                tabuleiro[1][1] == tabuleiro[2][0]
            )
        )
    ):
        print(f'{tabuleiro[1][1]} GANHOU!!!')
        return True
    
    """ Se não teve ganhador em nenhuma forma """    
    return False

def temEmpate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                return False
    print('Acabou empatado!')
    return True

while True:
    print(f'Jogador da vez: {jogador}')
    try:
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        jogador = jogada(linha, coluna)
    except (ValueError, IndexError):
        print('Digite valores numéricos entre 0 e 2')
    exibeTabuleiro()
    if temGanhador() or temEmpate():
        break

    
