"""
1. **Caça ao tesouro espacial**
Um tesouro está escondido em um planeta misterioso. Ele está em alguma linha e coluna de um mapa 4x4. Você tem 5 chances para tentar adivinhar onde ele está!

👉 O que o programa deve fazer:

- Criar um tabuleiro 3x3 com espaços vazios (listas dentro de listas);
- Definir uma posição fixa para o tesouro (por exemplo: linha 1, coluna 2);
- Pedir ao jogador para chutar linha e coluna (valores entre 0 e 2);
- Atualizar o tabuleiro a cada tentativa:
    - Marcar com 'X' os espaços já tentados.
    - Marcar com '💎' quando o tesouro for encontrado.
- Mostrar uma mensagem se:
    - O jogador acertar o local do tesouro;
    - O jogador errar;
    - O jogador tentar uma posição inválida;
    - O jogador já tiver tentado aquele espaço;
- Após 5 tentativas, encerrar o jogo e revelar a localização do tesouro.

- 💡 Dicas:
    - Lembre que as linhas e colunas começam do 0 ao 2;
    - Use `if` para verificar se o chute foi correto;
    - Use `else` para marcar tentativas erradas com um 'X';
    - Use `for` para controlar o número de tentativas (5);
    - Crie uma função para exibir o tabuleiro com print(), isso organiza o código!
    - Evite deixar que o aluno chute fora dos limites: use uma verificação com if;
"""
import os
os.system('cls')

# Define onde o 'tesouro' está:
treasure_line = 1
treasure_column = 1

# Tabuleiro 3x3:
tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Função para exibir o tabuleiro:
def exibeTabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)


tesouro_encontrado = False
# Loop que permite o jogador realizar os 'chutes' e o código retornará o tabuleiro com as 'posições' marcadas com X (se não tiver tesouro) e 💎 caso tenha tesouro
for tentativa in range(5):
    os.system('cls') # Limpa tudo o que estava antes no terminal

    exibeTabuleiro(tabuleiro)# Redesenha o tabuleiro no estado atual para o jogador ver

    print(f'\n--- Tentativa {tentativa + 1} de 5 ---')# Mostra as informações das novas tentativas

    attempt_line = int(input('Digite um valor de 0 a 2 para linha: '))# Pede para o jogador uma linha de 0 a 2 para buscar o tesouro
    attempt_column = int(input('Digite um valor de 0 a 2 para coluna: '))# Pede para o jogador a coluna de 0 a 2.
    
    if attempt_line < 0 or attempt_line > 2 or attempt_column < 0 or attempt_column > 2:# Condicional que processa e retorna "Jogada inválida" caso as entradas sejam diferentes de 0, 1 e 2
        print('Jogada inválida!')
    else:
        if attempt_line == treasure_line and attempt_column == treasure_column:# Caso as entradas sejam válidas (0, 1, 2)
            tabuleiro[attempt_line][attempt_column] = '💎' # Valida o tesouro no tabuleiro, na posição 1, 1
            os.system('cls')# Limpa o terminal
            exibeTabuleiro(tabuleiro)# Redesenha o tabuleiro para o jogador
            print('Você encontrou o tesouro 💎! Parabéns.')
            tesouro_encontrado = True
            break # Sai do programa.
        else:
            tabuleiro[attempt_line][attempt_column] = 'X' # Caso o jogador coloque entradas diferentes de 1,1 (posição do tesouro), será colocado um X na posição selecionada.
            print('Você errou! Planeta vazio.')
        exibeTabuleiro(tabuleiro) # Exibe o tabuleiro com as posições selecionadas pelo jogador
        

if not tesouro_encontrado:
    print('Suas tentativas acabaram! Boa sorte na próxima.')