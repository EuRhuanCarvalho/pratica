print('Bem vindo ao Caixa eletrônico.py Bank')
print('_' * 50)
restart = ('Y')
chances = 3
saldo = 999.75

while chances >= 0:
    senha = int(input('Por favor insira sua senha de 4 digitos: '))
    if senha == (1234):
        print('Senha correta')
        print('*', '_' * 50, '*')

        while restart not in ('não', 'NÃO', 'n', 'N'):
            print('Pressione 1 para ver o seu saldo')
            print('Pressione 2 para sacar')
            print('Pressione 3 para realizar um depósito')
            print('Pressione 4 para retirar o cartão\n')
            opcao = int(input('Qual a opção escolhida?: '))

            if opcao == 1:
                print('Seu saldo é R$ ', saldo)
                restart = input('Você gostaria de voltar?: ')
                if restart in ('não', 'NÃO', 'n', 'N'):
                    print('Obrigado!')
                    break

            elif opcao == 2:
                opcao2 = ('Y')
                saque = float(input(
                    'Qual valor você gostaria de sacar? \n10, \n20, \n30, \n40, \n50, \n60, \n80, \n100:'))
                if saque in [10, 20, 30, 40, 50, 60, 80, 100]:
                    saldo = saldo - saque
                    print('\nSeu saldo agora é R$: ', saldo)
                    restart = input('Você gostaria de voltar?: ')
                    if restart in ('não', 'NÃO', 'n', 'N'):
                        print('Obrigado!')
                        break
                elif saque != [10, 20, 30, 40, 50, 60, 80, 100]:
                    print('Valor inválido, por favor tente novamente\n')
                    restart = ('Y')
                elif saque == 1:
                    saque = float(input('Por favor insira o valor desejado: '))

            elif opcao == 3:
                deposito = float(input('Quanto você deseja depositar?: '))
                saldo = saldo + deposito
                print('\nSeu saldo agora é R$: ', saldo)
                restart = input('Você gostaria de voltar?: ')
                if restart in ('não', 'NÃO', 'n', 'N'):
                    print('Obrigado!')
                    break

            elif opcao == 4:
                print('Por favor, aguarde enquanto seu cartão é devolvido...\n')
                print('Obrigado por utilizar os nossos serviços')
                break
            else:
                print('Por favor digite o número correto. \n')
                restart = ('Y')

    elif senha != ('1234'):
        print('Senha incorreta')
        chances -= 1
        if chances == 0:
            print('\nConta bloqueada, contate o gerente da sua conta')
            break
