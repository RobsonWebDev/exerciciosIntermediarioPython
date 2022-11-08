dados = []
cont = 0
maior = menor = 0

while True:
    pessoas = []

    nome = str(input('digite um nome: '))
    cont += 1
    peso = float(input('digite o peso: '))

    pessoas.append(nome)
    pessoas.append(peso)

    if len(dados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    dados.append(pessoas[:])

    sair = int(input('digite 0 para sair: '))

    if sair == 0:
        break

print(f'foram cadstrados {cont} pessoas.')
print(f'o maior peso foir de {maior}kg. peso de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'o menor peso foi de {menor}kg. peso de ', end='')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')