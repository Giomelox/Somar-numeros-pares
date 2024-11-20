print('\nPreciso que você escolha dois números *inteiros*\npara que eu pegue o intervalo de número entre eles.\n')

primeiro_numero = int(input('Digite o primeiro número: '))

segundo_numero = int(input('Digite o segundo número: '))

soma_pares = 0

for x in range(primeiro_numero, segundo_numero):
    if x % 2 == 0:
        soma_pares += x 

if soma_pares:
    print(f'\nA soma dos números pares é: {soma_pares}')
else:
    print('\nNão há números pares no intervalo escolhido')

