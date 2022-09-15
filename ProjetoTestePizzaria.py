#Apresentação
print('\033[1;31m*\033[0m' * 52)
print('\033[1;93mBem vindo a pizzaria do Nono Diego Silveira da Silva\033[0m') #Identificador pessoal
print('\033[1;31m*\033[0m' * 52)

print('-.-' * 10, 'Cardápio', '-.-' * 10)
print('** Sabores, Tamanhos e Valores **\n (21) Napolitana -> [M]R$ 20,00 / [G]R$ 26,00\n (22) Margherita ->'
            ' [M]R$ 20,00 / [G]R$ 26,00\n (23) Calabresa -> [M]R$ 25,00 / [G]R$ 32,50\n '
            '(24) Toscana -> [M]R$ 30,00 / [G]R$ 39,00\n (25) Portuguesa -> [M] R$ 30,00 / [G]R$ 39,00')
print('-.-' * 23)

#variaveis dos preços médios e grandes
napm = 20
napg = 26
margm = 20
margg = 26
calm = 25
calg = 32.50
tosm = 30
tosg = 39
portm = 30
portg = 39

#Código
valor = 0
while True:
    tamanho = input('selecione o tamanho que deseja - [M] para Média e [G] para Grande: ').upper()
    if tamanho == ('M'):
        codigo = int(input('Selecione o código do sabor desejado: '))
        if codigo == 21:
            valor = valor + napm
            print('Você pediu uma pizza \033[1;32mNAPOLITANA\033[0m')
        elif codigo == 22:
            valor = valor + margm
            print('Você pediu uma pizza \033[1;32mMARGHERITA\033[0m')
        elif codigo == 23:
            valor = valor + calm
            print('Você pediu uma pizza \033[1;32mCALABRESA\033[0m')
        elif codigo == 24:
            valor = valor + tosm
            print('Você pediu uma pizza \033[1;32mTOSCANA\033[0m')
        elif codigo == 25:
            valor = valor + portm
            print('Você pediu uma pizza \033[1;32mPORTUGUESA\033[0m')
        else:
            print('\033[1;31mOpção invalida, tente novamente.\033[0m')
            continue
        continuar = input('Deseja mais algo?\n'
                          '[S] para SIM / [N] para NÃO: ').upper()
        if continuar == 'S':
            continue
        elif continuar == 'N':
            print('\033[1;34mObrigado por escolher a pizzaria do Nono Diego Silveira da Silva.\n '
                  'O valor total do seu pedido é de R$ {:.2f}\033[0m'.format(valor))
            break
    elif tamanho == ('G'):
        codigo = int(input('Selecione o código do sabor desejado: '))
        if codigo == 21:
            valor = valor + napm
            print('Você pediu uma pizza \033[1;32mNAPOLITANA\033[0m')
        elif codigo == 22:
            valor = valor + margg
            print('Você pediu uma pizza \033[1;32mMARGHERITA\033[0m')
        elif codigo == 23:
            valor = valor + calg
            print('Você pediu uma pizza \033[1;32mCALABRESA\033[0m')
        elif codigo == 24:
            valor = valor + tosg
            print('Você pediu uma pizza \033[1;32mTOSCANA\033[0m')
        elif codigo == 25:
            valor = valor + portg
            print('Você pediu uma pizza \033[1;32mPORTUGUESA\033[0m')
        else:
            print('Opção invalida, tente novamente')
            continue
        conti = input('Deseja mais algo?\n '
                      '[S] para SIM / [N] para NÃO: ').upper()
        if conti == 'S':
            continue
        elif conti == 'N':
            print('\033[1;34mObrigado por escolher a pizzaria do Nono Diego Silveira da Silva.\n '
                  'O valor total do seu pedido é de R$ {:.2f}\033[0m'.format(valor))
            break
    else:
        print('Opção invalida, tente novamente.')