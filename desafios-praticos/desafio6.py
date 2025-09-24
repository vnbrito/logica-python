import os
os.system('cls')

print('Bem vindo ao Quiz de Conhecimentos Gerais!')
ponto = 0
erros = 0

perguntas = [
    ['Qual a capital do brasil?', 'Brasília'],
    ['Qual animal que faz Au Au?', 'Cachorro'],
    ['Quem descobriu o Brasil?', 'Pedro Alvarez Cabral'],
    ['Qual a representação do Ouro na Tabela Periódica?', 'Au'],
    ['Qual animal que faz pocotó?', 'Cavalo']
    ]

for pergunta_resposta in perguntas:
    pergunta_atual = pergunta_resposta[0]
    resposta_correta = pergunta_resposta[1]
    print(pergunta_atual)
    resposta_usuario = input('Digite a sua resposta: ')
    if resposta_usuario.lower() == resposta_correta.lower():
        print('Você acertou!')
        print()
        acertos = ponto + 1
        ponto = ponto + 1
    else:
        print('Você errou!')
        print()
        erros = erros + 1

porcentagem_acertos = ponto * 20

print(f'Você acertou {ponto} perguntas e errou {erros}.')
print(f'Parabéns, você acertou {porcentagem_acertos}% do Quiz!')
        