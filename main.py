from controller import *

pessoa1 = {'ID': 5, 'nome': 'Georgia2', 'cpf': '123000000'}

print(existePessoa(pessoa1))


while True:
    menu()
    opcaoMenu = input("Informe uma opção: ")
    
    match opcaoMenu:

        case '1':
            usuarioCheckin = input("Informe o nome do usuário: ")
            if buscaPessoa(usuarioCheckin):
                editaPessoa(buscaPessoa(usuarioCheckin),True)
            else:
                print("Usuário não encontrado deseja cadastrar?")
                opcaoCadastrar = input("S ou N: ")
                if opcaoCadastrar.lower() == "s":
                    cadastraPessoa(pegaDadosCadastro())

        case '2':
            usuarioCheckin = input("Informe o nome do usuário: ")
            if buscaPessoa(usuarioCheckin):
                print(buscaPessoa(usuarioCheckin))
                editaPessoa(buscaPessoa(usuarioCheckin),False)
                input()
            else:
                print("Usuario não encontrado")
                input()
        case '3':
            relatorioPessoas()
        case '4':
            buscaPessoaMenu = input("Digite o nome do usuário: ")
            print(buscaPessoa(buscaPessoaMenu))
            input()
            
        case '5':
            break
        case _:
            pass