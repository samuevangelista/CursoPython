n = 1
par = impar = 0
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    if n != 0 :
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
    r = str(input('Quer continuar? [S/N]:')).upper()
print('Vodigitou {} numeros pares e {} numeros impares!'.format(par, impar))