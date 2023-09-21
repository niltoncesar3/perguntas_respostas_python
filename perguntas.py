"""
EXERCICIO - SISTEMA DE PERGUNTAS E RESPOSTAS
"""

perguntas = [
    {
        'Pergunta' : 'Quanto é 2 + 2? ',
        'Opções' : ['1','2','3','4'],
        'Resposta': '4',
    },
    {
        'Pergunta' : 'Quanto é 5 + 5? ',
        'Opções' : ['10','20','35','45'],
        'Resposta': '10',
    },
    {
        'Pergunta' : 'Quanto é 20 / 4? ',
        'Opções' : ['17','28','5','10'],
        'Resposta': '5',
    }
]

qtd_acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i,opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    
    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou X')

    print()

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')

    
