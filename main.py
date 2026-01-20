from funções import criar_senha, gerador_senha


def menu():
    while True:
        print('*' * 40)
        print(f' Gerenciador de senhas')
        print('*' * 40)

        print(f'1 - Digitar a senha')
        print(f'2 - Gerador de senha')
        print(f'3 - Sair')

        opcao = (input(f'Digite a opção escolhida: '))
        print(opcao)

        if opcao == "1":
            criar_senha()
        elif opcao == "2":
            gerador_senha()
        elif opcao == "3":
            print(f'Saindo do sistema...')
            break


menu()