import os
from classes import *

locadora = Locadora()

def ls():
    os.system('pause...')
    os.system('cls')


def cadastrar_cliente(locadora):
    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    cliente = Clientes(nome, cpf)
    locadora.cadastrar_cliente(cliente)
    print("Cliente cadastrado com sucesso!")

def cadastrarItem(self, item: Itens):
        self.__itens.append(item)
        print(f"Item {item.getTitulo()} cadastrado com sucesso!")

def cadastrar_filme(locadora):
        try:
            titulo = input("Título: ")
            genero = input("Gênero: ")
            duracao = int(input("Duração (minutos): "))
            filme = Filme(titulo, genero, duracao)
            locadora.cadastrarItem(filme)
            print(f"Filme '{filme.getTitulo()}' cadastrado com código {filme.getCodigo()}!")
            
        except ValueError:
            print(" Entrada inválida!")

def cadastrar_jogo(locadora):
    try:
        titulo = input ('Título:')
        plataforma = input ('Gênero:')
    
    except ValueError:
        print('Entrada inválida!')

def listar_clientes(locadora):
    print("\n Clientes:")
    for nome, cpf in locadora.listarClientes():
        print(f"- {nome} (CPF: {cpf})")

def listar_itens(locadora):
    print("\n Itens:")
    for titulo, status in locadora.listarItens():
        print(f"- {titulo} ({status})")

def locar_item(locadora):
    cpf = input("CPF do cliente: ")
    codigo = int(input("Código do item: "))

    cliente = locadora.buscar_cliente(cpf)
    item = locadora.buscar_item(codigo)

    if cliente and item:
        if cliente.locar(item):
            print("Item alugado com sucesso!")
        else:
            print("Item indisponível!")
    else:
        print("Cliente ou item não encontrado.")


def devolver_item(locadora):
    cpf = input("CPF do cliente: ")
    codigo = int(input("Código do item: "))

    cliente = locadora.buscar_cliente(cpf)
    item = locadora.buscar_item(codigo)

    if cliente and item:
        if cliente.devolver(item):
            print("Item devolvido com sucesso!")
        else:
            print("Este cliente não alugou este item.")
    else:
        print("Cliente ou item não encontrado.")