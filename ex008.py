num = []

while True:
    n = int(input('Digite um valor: '))

    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado nao foi adicionado.')

    r = str(input('Quer continuar? [S/N]'))

    if r in 'Nn':
        break

print(num)