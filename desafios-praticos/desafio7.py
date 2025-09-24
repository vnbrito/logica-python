"""
1. **Número secreto**
Escolha um número fixo e peça para o usuário tentar adivinhar até acertar (de verdade).

👉 O que o programa deve fazer:

- Pedir para o jogador digitar um número;
- Repetir essa pergunta até ele acertar o número secreto;
- Contar quantas tentativas ele fez;
- Mostrar uma mensagem de parabéns e quantas tentativas ele fez até acertar.
- 💡 Dicas:
    - Use uma variável para guardar o número secreto;
    - Use um laço while para repetir o processo enquanto o jogador não acertar;
    - Crie uma variável tentativas e incremente ela com +1 a cada tentativa errada;
    - Use o comando input() para receber o chute do jogador;
    - Compare o chute com o número secreto usando if.
"""
import os
os.system('cls')

secretNumber = 7
userAttempts = 0
userInput = int(input('Digite um número aleatório: '))
userAttempts = userAttempts + 1

while userInput != secretNumber:
    print('Você errou! Tente novamente.')
    userAttempts = userAttempts + 1
    userInput = int(input('Digite um número aleatório: '))
    
    if userInput == secretNumber:
        print(f'Parabéns! Você acertou! O número secreto era {secretNumber}. Total de tentativas até acertar: {userAttempts}')
    
        
        