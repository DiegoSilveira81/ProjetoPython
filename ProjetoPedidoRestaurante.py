def volumeFeijoada(): #Exigencia1
    while True:
        try:
            volumfe = float(input('Informe a quantidade de feijoada que você deseja (ml): '))
            if volumfe < 300:
                print('\033[1;31mNão aceitamos pedidos menores que 300ml, tente novamente\033[0m')
            elif 300 <= volumfe <= 5000:
                return volumfe * 0.08
            elif volumfe > 5000:
                print('\033[1;31mVolume acima do permitido, tente novamente.\033[0m')
            else:
                print('\033[1;31mOpção invalida, tente novamente.\033[0m')
                continue
        except ValueError:
            print('\033[1;31mVolume acima do permitido, tente novamente.\033[0m')
            continue
def opcaoFeijoada(): #Exigencia2
    while True:
        try:
            optfe = input('Selecione a opção de tamanho da sua feijoada.\n '
                          '\033[1;32mB - Básica (Feijão + paiol + costelinha)\033[0m\n '
                          '\033[1;33mP - Premium (Feijão + paiol + costelinha + partes de porco)\033[0m\n '
                          '\033[1;34mS - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)\033[0m\n '
                          'Selecione sua opção: ').upper()
            if optfe == 'B':
                return 1.00
            elif optfe == 'P':
                return 1.25
            elif optfe == 'S':
                return 1.50
            else:
                print('\033[1;31mOpção invalida, tente novamente.\033[0m')
                continue
        except ValueError:
            print('\033[1;31mOpção invalida, tente novamente.\033[0m')
            continue
def acompanhamentoFeijoada(): #Exigencia3
    acumulador = 0
    while True:
        try:
            acompfe = input('Selecione um acompanhamento:\n '
                            '\033[1;31m0 - Não desejo acompnhamentos. Encerrar pedido.\033[0m\n '
                            '\033[1;32m1 - 200g de arroz\033[0m\n '
                            '\033[1;33m2 - 150g de farofa especial\033[0m\n '
                            '\033[1;34m3 - 100g de couve cozida\033[0m\n '
                            '\033[1;35m4 - 1 laranja descascada\033[0m\n '
                            'Informe o acompanhamento desejado: ')
            if acompfe == '0':
                return acumulador
            elif acompfe == '1':
                acumulador = acumulador + 5.00
            elif acompfe == '2':
                acumulador = acumulador + 6.00
            elif acompfe == '3':
                acumulador = acumulador + 7.00
            elif acompfe == '4':
                acumulador = acumulador + 3.00
            else:
                print('\033[1;31mOpção invalida, tente novamente.\033[0m')
                continue
        except ValueError:
            print('\033[1;31mOpção invalida, tente novamente.\033[0m')
            continue
print('\033[1;33mBem vindo a Feijoada do Sinhô Diego Silveira da Silva\n'
      'Monte a sua feijoada!\033[0m') #Identificador Pessoal
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acomp = acompanhamentoFeijoada()
total = volume * opcao + acomp
print('\033[1;36mO valor total é de R$ {:.2f}\n'
      'Obrigado e bom apetite.\033[0m'.format(total))