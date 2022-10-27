import os
#from random import randrange
#import linecache
import ast

os.system('cls' if os.name == 'nt' else 'clear')

def buscaPessoa(nome): #recebe o nome da pessoa e retorna a pessoa ou False se não encontrar.

    with open('pessoas.txt', 'r') as reader:

        for line in reader:
            aux = ast.literal_eval(line)
            if aux['nome'] == nome:
                return line
            
    return False



def cadastraPessoa(pessoa): #Recebe uma pessoa [Dicionário] e converte para string e salva no final do arquivo.
    with open('pessoas.txt', 'a') as writer:
        writer.write(f'\n{pessoa}')


#Encontra a pessoa no arquivo e atualiza os dados desta pessoa. 
#Se check for passado ele altera o status de checIn/Out da pessoa;
def editaPessoa(pessoa, check=False):
    
    with open('pessoas.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
        pessoa = eval(pessoa)
        if check:
            print(pessoa)
            pessoa['checkin'] = 1
        else:
            pessoa['checkin'] = 0
            
        for i in range (len(data)):
            aux = eval(data[i])

            #print(aux['ID'])
            #print(str(pessoa))
            
            if aux['ID'] == pessoa['ID']:
                data[i] = str(pessoa)+"\n"

    # and write everything back
    with open('pessoas.txt', 'w') as file:
        file.writelines( data )
    

def existePessoa(pessoa): #Recebe o [dicionario] pessoa e verifica se ela existe no arquivo e retorna apenas true or false
    with open('pessoas.txt', 'r') as reader:

        for line in reader:
            aux = ast.literal_eval(line)
            if aux['ID'] == pessoa['ID'] or aux['nome'] == pessoa['nome']:
                return True
    return False

def relatorioPessoas():
    pessoasAretornar = []
    
    with open('pessoas.txt', 'r') as reader:
        
        for line in reader:
            aux = ast.literal_eval(line)
            if aux['checkin'] == '1':
                pessoasAretornar.append(aux)
                #print(aux)
        return pessoasAretornar

def mostraPessoasBonito(listaPessoas):
    print("\n")
    for line in listaPessoas:
        tabID = " "*(5-len(str(line["ID"])))
        print("ID:" + str(line["ID"]) + tabID + " Nome: " + line["nome"])
    print("\n")



def menu():
    print("1- Fazer CheckIn:")
    print("2- Fazer CheckOut")
    print("3- Relatorio de hospedes")
    print("4- Procurar hospede")
    print("5- Sair do programa")
    
def pegaDadosCadastro():
    id = input("ID: ")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    checkIn = input("Ja fazer o checkIn? S ou N: ")
    if checkIn.lower() == "s":
        checkIn = '1'
    else:
        checkIn = '0'
    pessoa = ("{" + f"'ID': {id}, 'nome': '{nome}', 'cpf': '{cpf}', 'checkin':'{checkIn}'"+"}")
    return pessoa