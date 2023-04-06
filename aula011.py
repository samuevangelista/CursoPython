print('\033[1;31;43mOlá, Mundo\033[m')
print('\033[4;30;45mOlá, Mundo\033[m')
print('\033[7;30;44mOlá, Mundo\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

nome = 'Samuel'
print('Olá, é um prazer te conhecer {} {} {}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
        'amarelo':'\033[33m',
        'amarelo':'\033[7;30m'}
print('Ola mundo, nome {} {} {} !!!'.format(cores['amarelo'], nome, cores['limpa']))