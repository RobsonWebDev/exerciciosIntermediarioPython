num = (int(input('digite um numero: ')),int(input('digite outro numero: ')),
       int(input('digite mais um numero: ')),int(input('digite o ultimo numero: ')))

print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
   print(f'O valor 3 apareceu na {num.index(3)+1}ª posicao')
else:
   print(f'O valor 3 nao foi digitado')

print('Os valores pares foram ', end='')
for n in num:
   if n % 2 == 0:
       print(n, end=' ')