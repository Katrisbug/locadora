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

def cadastrar_itens(locadora):
    tipo = input("O item é um Filme (F) ou Jogo (J)? ").strip().upper()

    if tipo == "F":
        cadastrar_filme(locadora)

    elif tipo == "J":
        cadastrar_jogo(locadora) 

    else:
        print("Opção inválida! Digite apenas F para Filme ou J para Jogo.")

def cadastrar_filme(locadora):
        try:
            titulo = input("Título: ")
            genero = input("Gênero: ")
            duracao = int(input("Duração (minutos): "))
            codigo = int(input("Código do filme: "))
            filme = Filme(genero, duracao, codigo, titulo)
            locadora.cadastrar_itens(Filme)
            print(f"Filme '{filme.getTitulo()}' cadastrado com código {filme.getCodigo()}!")
            
        except ValueError:
            print(" Entrada inválida!")

def cadastrar_jogo(locadora):
    try:
        titulo = input("Título: ")
        plataforma = input("Plataforma: ")
        faixa_etaria = int(input("Faixa etária: "))
        codigo = int(input("Código do jogo: "))
        jogo = Jogo(plataforma, faixa_etaria, codigo, titulo)
        locadora.cadastrar_itens(Jogo)
        print(f"Jogo '{jogo.getTitulo()}' cadastrado com código {jogo.getCodigo()}!")

    except ValueError:
        print("Entrada inválida!")

def listar_clientes(locadora):
    print("\n Clientes:")
    for nome, cpf in locadora.listar_clientes():
        print(f"- {nome} (CPF: {cpf})")

def listar_itens(locadora):
    print("\n Itens:")
    for titulo, status in locadora.listar_itens():
        print(f"- {titulo} ({status})")

def locar_item(locadora):
    cpf = input("CPF do cliente: ")
    try:
        codigo = int(input("Código do item: "))

    except ValueError:
        print("Código inválido")
        return
    
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
    try:
        codigo = int(input("Código do item: "))

    except ValueError:
        print("Código inválido")
        return

    cliente = locadora.buscar_cliente(cpf)
    item = locadora.buscar_item(codigo)

    if cliente and item:
        if cliente.devolver(item):
            print("Item devolvido com sucesso!")
        else:
            print("Este cliente não alugou este item.")
    else:
        print("Cliente ou item não encontrado.")