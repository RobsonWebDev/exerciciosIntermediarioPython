num = list()
num_par = list()
num_impar = list()
cont = 0
add = 0
while True:
    n = int(input('Digite um valor: '))
    cont += 1
    if n not in num:
        num.append(n)
        add += 1
        print('Valor adicionado na sua lista')

        if n % 2 == 0:
            num_par.append(n)
        else:
            num_impar.append(n)
    else:
        print('Valor Duplicado nao foi adicionado')

    r = str(input('Quer continuar? [S/N]'))

    if r in 'Nn':
        break

    else:
        continue

sobra = cont - add

num_decrescente = num[:]
num_decrescente.sort(reverse=True)

if 5 in num:
    print(f'O numero 5 foi digitado e esta na {num.index(5)+1}ª posicao.')
if 5 not in num:
    print(f'O numero 5 nao foi digitado.')


print(f'Foram digitados {cont} numeros')
print(f'Dos {cont} numeros somente {add} numeros foram adicionados.')
print(f'Dos {cont} numeros somente {sobra} numeros nao foram adicionados')
print(f'Os numeros adicionados foi: {num}, dando um total de {len(num)} itens na sua lista'
      f'\nDo maior para o menor fica: {num_decrescente}')
print(f'Sua lista teve {len(num_par)} numeros pares sendo eles: {num_par}')
print(f'Sua lista teve {len(num_impar)} numeros impares sendo eles: {num_impar}')
