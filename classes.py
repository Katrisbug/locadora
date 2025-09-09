class Itens:
    def __init__(self, codigo:int, titulo:str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponivel = True

    def alugar (self):
        if self.__disponivel:
            self.__disponivel = False
            return f'O item {self.__titulo} alugado com sucesso!'
        else:
            return f'O item {self.__titulo} não esta disponivel para alugar.'
    

    def devolver (self):
        if not self.__disponivel:
            self.__disponivel = True
            return f'O item {self.__titulo} foi devolvido com sucesso.'
        else:
            return f'O item {self.__titulo} está disponivel.'

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
        self.__itens_Locados = []

    def locar (self, item:Itens):
            item.__alugar()
            self.__itens_Locados.append(Itens)


    def devolver (self, item:Itens):
        if item in self.__itens_Locados:
            item.__devolver()
            self.__itens_Locados.remove(Itens)
            return True
        return False

    def listar_itens (self):
        return self.__itens_Locados
        

class Locadora:
    def __init__ (self):
        self.__clientes = []
        self.__itens = []

    def cadastro_cliente (self, clientes: Clientes):
        self.__clientes.append(Clientes)

    def cadastro_itens (self):
        self.__item.append (Itens)

    def listar_clientes (self,):
        if not self.__clientes:
            return 'Nenhum cliente cadastrado.'

    def listar_itens (self):
        for item in self.__itens_Locados:
            return (Itens)



    