from Pessoas import Pessoas
lista = []
n = ' '
while n not in 'Nn':
    try:
        x = int(input("""Escolha uma opção:
1-Criar nova pessoa
2-Fazer alguém comer
3-Fazer alguém falar   
4-Fazer alguém parar de comer
5-Fazer alguém parar de falar
"""))
    except:
        print('Opção inválida!')
        continue
    if x == 1:
        nome = str(input('Nome:'))
        try:
            idade = int(input('Idade: '))
        except:
            print('IDADE INVÁLIDA!')
            continue
        p1 = Pessoas(nome,idade)
        lista.append(p1)
    if x == 2:
        print('Esolha quem você deseja fazer comer')
        for c in range(0,len(lista)):
            print(f'{c+1} - {lista[c].getNome()}')
        try:
            scan = int(input())
            comida = str(input('Qual comida?'))
            lista[scan - 1].comer(comida)
        except:
            print('OPÇÃO INVÁLIDA!')
            continue
    if x == 3:
        print('Esolha quem você deseja fazer falar')
        for c in range(0,len(lista)):
            print(f'{c+1} - {lista[c].getNome()}')
        try:
            scan = int(input())
            fala = str(input('Sobre o que quer falar?'))
            lista[scan - 1].falar(fala)
        except:
            print('OPÇÃO INVÁLIDA!')
            continue

    if x == 4:
        print('Esolha quem você deseja fazer parar de comer')
        for c in range(0, len(lista)):
            print(f'{c + 1} - {lista[c].getNome()}')
        try:
            scan = int(input())
            lista[scan - 1].parar_Comer()
        except:
            print('OPÇÃO INVÁLIDA!')
            continue

    if x == 5:
        print('Esolha quem você deseja fazer parar de falar')
        for c in range(0, len(lista)):
            print(f'{c + 1} - {lista[c].getNome()}')
        try:
            scan = int(input())
            lista[scan - 1].parar_Falar()
        except:
            print('OPÇÃO INVÁLIDA!')
            continue
    n = str(input('Deseja continuar? [S/N] '))
    while n not in 'SsNn':
        n = str(input('Comando inválido! Deseja continuar? [S/N] '))

for c in range(0,len(lista)):
    if lista[c].getComendo() == True:
        print(f'{lista[c].getNome()} terminou comendo!')
    elif lista[c].getFalando() == True:
        print(f'{lista[c].getNome()} terminou falando!')
    else:
        print(f'{lista[c].getNome()} terminou sem estar comendo nem falando!')