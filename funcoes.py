def cadastrar_cliente(locadora: Locadora):
    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    cliente = Cliente(nome, cpf)
    locadora.cadastrarCliente(cliente)
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