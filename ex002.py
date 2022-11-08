tabelabrasileirao2022 = ('corinthias', 'palmeiras', 'sao paulo', 'botafogo', 'santos', 'atletico-mg',
                         'coritiba', 'fluminense', 'america-mg', 'avai', 'bragantino', 'internacional',
                         'athletico-pr', 'flamengo', 'goias', 'cuiaba', 'juventude', 'ceara-sc',
                         'atletico-go', 'fortaleza')

for tabela in tabelabrasileirao2022:

    melhorcolocaco = tabelabrasileirao2022[0:6]
    zonaderebaixamento = tabelabrasileirao2022[16:]
    ordemalfabetica = sorted(tabelabrasileirao2022)

    print('-=' * 8)
    print(f'[A] TABELA DO BRASILEIRAO 2022 ',
          f'[B] OS CINCOS PRIMEIROS DO BRASILEIRAO 2022',
          f'[C] ZONA DE REBAIXAMENTO, BRASILEIRAO 2022',
          f'[D] EXIBIR TABELA EM ORDEM ALFABETICA',
          f'[E] SAIR')
    print('-=' * 8)

    user = str(input('Digite a opção desejada: '))

    if user == 'a':
        print(tabelabrasileirao2022)

    elif user == 'b':
        print(melhorcolocaco)

    elif user == 'c':
        print(zonaderebaixamento)

    elif user == 'd':
        print(ordemalfabetica)

    elif user == 'e':
        break

    else:
        print('erro! Tente Novamente. ')
        continue