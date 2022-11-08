num = []

for x in range(0, 5):
    num.append(int(input('digite um valor: ')))

print(f'Voce digitou os valores: {num}')
print(f'e o maior numero foi o {max(num)} aparecendo na {num.index(max(num))+1}ª posição,'
      f'\ne o menor foi o {min(num)} aparecendo na {num.index(min(num))+1}ª posição.')