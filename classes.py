class Itens:
    def __init__(self, codigo:int, titulo:str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponivel = True

    def alugar (self):
        if self.__disponivel:
            self.__disponivel : False
            print(f'O item {self.__titulo} alugado com sucesso!')
        else:
            print(f'O item {self.__titulo} não esta disponivel para alugar.')
    

    def devolver (self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f'O item {self.__titulo} foi devolvido com sucesso.')
        else:
            print(f'O item {self.__titulo} está disponível.')

class Filme (Itens):
    def __init__(self, genero:str, duracao:int):
        self.__genero = genero
        self.__duracao = duracao
    

class Jogo (Itens):
    def __init__(self, plataforma:str, faixa_etaria:int):
        self.__plataforma = plataforma
        self.__faixa_etaria = faixa_etaria

class Clientes:
    def __init__(self, nome:str, cpf:str):
        self.__nome = nome
        self.__cpf = cpf
        self.__itens_locados = []

    def locar (Itens):
        pass

    def devolver (Itens):
        pass

    listar_itens()

class Locadora:
    def __init__ (self):
        self.__clientes = []
        self.__itens = []

    def cadastro_cliente (self, ):
        pass

    def cadastro_itens (self):
        pass

    def listar_clientes (self,):
        pass

    def listar_itens (self):
        pass



    