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
    def __init__(self, genero:str, duracao:int, codigo:int, titulo:str):
        Itens.__init__(self, codigo, titulo)
        self.__genero = genero
        self.__duracao = duracao
    

class Jogo (Itens):
    def __init__(self, plataforma:str, faixa_etaria:int, codigo:int, titulo:str):
        Itens.__init__(self, codigo, titulo)
        self.__plataforma = plataforma
        self.__faixa_etaria = faixa_etaria

class Clientes:
    def __init__(self, nome:str, cpf:str):
        self.__nome = nome
        self.__cpf = cpf
        self.__itens_Locados = []

    def locar (self, item:Itens):
            item.__alugar()
            self.__itens_Locados.append(item)


    def devolver (self, item:Itens):
        if item in self.__itens_Locados:
            item.__devolver()
            self.__itens_Locados.remove(item)
            return True
        return False

    def listar_itens (self):
        return self.__itens_Locados
        

class Locadora:
    def __init__ (self, nome:str):
        self.__nome = nome
        self.__clientes = []
        self.__itens = []

    def cadastro_cliente (self, cliente: Clientes):
        self.__clientes.append(cliente)

    def cadastro_itens (self, item: Itens):
        self.__item.append (item)

    def listar_clientes (self,):
        if not self.__clientes:
            return 'Nenhum cliente cadastrado.'

    def listar_itens (self):
        for item in self.__itens_Locados:
            return (item)



    