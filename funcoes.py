import os
from classes import *

locadora = Locadora()

def ls():
    os.system('pause...')
    os.system('cls')


def cadastrar_cliente(locadora: Locadora):
    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    cliente = Clientes(nome, cpf)
    locadora.cadastrarClientes(cliente)
    print("Cliente cadastrado com sucesso!")

def cadastrar_item(locadora: Locadora):
    print("1 - Filme\n2 - Jogo")
    opc = input("Escolha o tipo de item: ")

    codigo = int(input("Código do item: "))
    titulo = input("Título: ")

    if opc == "1":
        genero = input("Gênero: ")
        duracao = int(input("Duração (minutos): "))
        item = Filme(codigo, titulo, genero, duracao)
    else:
        plataforma = input("Plataforma: ")
        faixa = int(input("Faixa etária: "))
        item = Jogo(codigo, titulo, plataforma, faixa)

    locadora.cadastrarItem(item)
    print("Item cadastrado com sucesso!")

def listar_clientes(locadora: Locadora):
    print("\n Clientes:")
    for nome, cpf in locadora.listarClientes():
        print(f"- {nome} (CPF: {cpf})")

def listar_itens(locadora: Locadora):
    print("\n Itens:")
    for titulo, status in locadora.listarItens():
        print(f"- {titulo} ({status})")

def locar_item(locadora: Locadora):
    cpf = input("CPF do cliente: ")
    codigo = int(input("Código do item: "))

    cliente = locadora.buscarCliente(cpf)
    item = locadora.buscarItem(codigo)

    if cliente and item:
        if cliente.locar(item):
            print("Item alugado com sucesso!")
        else:
            print("Item indisponível!")
    else:
        print("Cliente ou item não encontrado.")


def devolver_item(locadora: Locadora):
    cpf = input("CPF do cliente: ")
    codigo = int(input("Código do item: "))

    cliente = locadora.buscarCliente(cpf)
    item = locadora.buscarItem(codigo)

    if cliente and item:
        if cliente.devolver(item):
            print("Item devolvido com sucesso!")
        else:
            print("Este cliente não alugou este item.")
    else:
        print("Cliente ou item não encontrado.")