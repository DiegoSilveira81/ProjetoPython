from time import sleep
listaprod = []
def cadastrarProduto(codigo):
    print('\033[1;31mVocê Selecionou a opção CADASTRAR PRODUTO.\033[0m')
    print('O código do produto é: {:0>3}'.format(codigo))
    nomeprod = input('Informe o nome do PRODUTO: ').upper()
    marcaprod = input('Informe o nome do FABRICANTE: ').upper()
    valorprod = float(input('Informe o VALOR do produto: R$ '))
    dicionarioProduto = {'Código' : codigo,
                         'Nome '  : nomeprod,
                         'Marca'  : marcaprod,
                         'Valor'  : valorprod}
    listaprod.append(dicionarioProduto.copy())

def consultarProduto():
    while True:
        try:
            print('\033[1;31mVocê Selecionou a opção CONSULTAR PRODUTO.\033[0m')
            opConsultar = int(input('Informe a opção desejada:\n'
                                    '\033[1;32m[1] - Consultar todos os produtos.\033[0m\n'
                                    '\033[1;33m[2] - Consultar produto por código.\033[0m\n'
                                    '\033[1;34m[3] - Consultar produto por fabricante.\033[0m\n'
                                    '\033[1;35m[4] - Retornar.\033[0m\n'
                                    '\033[1;31mOpção desejada: \033[0m'))
            if opConsultar == 1:
                print('*' * 20)
                for produto in listaprod:
                    for key, value in produto.items():
                        print('{} : {}'.format(key, value))
                    print('*' * 20)
            elif opConsultar == 2:
                print('\033[1;31mVocê Selecionou a opção CONSULTAR PRODUTO POR CÓDIGO.\033[0m')
                entrada = int(input('Digite o código do produto: '))
                print('*' * 20)
                for produto in listaprod:
                    if(produto['Código'] == entrada):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))
                        print('*' * 20)
            elif opConsultar == 3:
                print('\033[1;31mVocê Selecionou a opção CONSULTAR PRODUTO POR FABRICANTE.\033[0m')
                entrada = input('Digite o fabricante: ').upper()
                print('*' * 20)
                for produto in listaprod:
                    if(produto['Marca'] == entrada):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))
                        print('*' * 20)
            elif opConsultar == 4:
                break
            else:
                print('Opção invalida.')
                continue
        except ValueError:
            print('Opção invalida, tente novamente.')
            continue
def removerProduto():
    print('\033[1;31mVocê selecionou a opção REMOVER PRODUTO.\033[0m')
    entrada = int(input('Digite o código do produto que deseja remover: '))
    for produto in listaprod:
        if(produto['Código'] == entrada):
            listaprod.remove(produto)
            print('Removendo produto....')
            sleep(5)
            print('Produto REMOVIDO com sucesso.')
        else:
            print('Código ou Produto inexistente.')
print('\033[1;32mBem vindo a mercearia Diego Silveira da Silva\033[0m')
registroProd = 0
while True:
    try:
        opt = int(input('\033[1;31mDigite a opção desejada:\n'
                        '[1] - Cadastrar Produto.\n'
                        '[2] - Consultar Produto.\n'
                        '[3] - Remover Produto.\n'
                        '[4] - Sair.\n'
                        'Informe sua opção: '))
        if opt == 1:
            registroProd = registroProd + 1
            cadastrarProduto(registroProd)
        elif opt == 2:
            consultarProduto()
        elif opt == 3:
            removerProduto()
        elif opt == 4:
            print('\033[1;34mPrograma Finalizado.\033[0m')
            break
        else:
            print('Opção invalida.')
            continue
    except ValueError:
        print('Opção invalida, tente novamente.')