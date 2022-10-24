import os
#from random import randrange
#import linecache
import ast

os.system('cls' if os.name == 'nt' else 'clear')

def buscaPessoa(id=0, nome=''): #recebe o ID ou nome da pessoa e retorna a pessoa ou False se não encontrar.

    with open('pessoas.txt', 'r') as reader:

        for line in reader:
            aux = ast.literal_eval(line)
            if aux['ID'] == id or aux['nome'] == nome:
                return line
            
    return False
            


def cadastraPessoa(pessoa): #Recebe uma pessoa [Dicionário] e converte para string e salva no final do arquivo.
    with open('pessoas.txt', 'a') as writer:
        writer.write(f'\n{pessoa}')

def editaPessoa(pessoa): #Encontra a pessoa no arquivo e atualiza os dados desta pessoa.
    
    with open('pessoas.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
        
        for i in range (len(data)):
            aux = eval(data[i])

            #print(aux['ID'])
            print(str(pessoa))
            
            if aux['ID'] == pessoa['ID']:
                data[i] = str(pessoa)+"\n"

    # and write everything back
    with open('pessoas.txt', 'w') as file:
        file.writelines( data )
    

def existePessoa(pessoa): #Recebe o [dicionario] pessoa e verifica se ela existe no arquivo e retorna apenas true or false
    pass




pessoa1 = {'ID': 3, 'nome': 'Georgia2', 'cpf': '123000000'}


editaPessoa(pessoa1)