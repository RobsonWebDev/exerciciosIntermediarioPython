tempAno = list()
tempMes = list()
cont = 0
while True:
    tempMes.append(str(input('DIgite o mes: ')))
    tempMes.append(int(input('Digite a Temperatura: ')))
    tempAno.append(tempMes[:])
    tempMes.clear()

    resp = str(input('Deseja Continuar? [s/n]  '))
    if resp in 'Nn':
        break
for mes, tM in tempAno:
    print(f'o mes de {mes} atingiu {tM}° graus neste ano!')
