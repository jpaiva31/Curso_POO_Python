def leint(a):
    while True:
        try:
            n = int(input(a))
        except:
            print ('Falhou! Digite um número inteiro válido! ')
            continue
        else:
            return n

def lefloat(a):
    while True:
        try:
            n = float(input(a))
        except:
            print ('Falhou! Digite um número real válido! ')
            continue
        else:
            return n
n1 = leint('Digite um valor: ')
n2 = lefloat('Digite um valor: ')
print('O valor inteiro digitado foi {} e o valor real foi {}'.format(n1,n2))
