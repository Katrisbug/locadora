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
        
    def is_disponivel(self):
        return self.__disponivel

    def set_disponivel(self, valor: bool):
        self.__disponivel = valor

    #gets de itens
    def getCodigo(self):
        return self.__codigo

    def getTitulo(self):
        return self.__titulo

class Filme (Itens):
    def __init__(self, genero:str, duracao:int, codigo:int, titulo:str):
        Itens.__init__(self, codigo, titulo)
        self.__genero = genero
        self.__duracao = duracao

    #gets de filme
    def getGenero(self):
        return self.__genero
    
    def getDuracao(self):
        return self.__duracao
    

class Jogo (Itens):
    def __init__(self, plataforma:str, faixa_etaria:int, codigo:int, titulo:str):
        Itens.__init__(self, codigo, titulo)
        self.__plataforma = plataforma
        self.__faixa_etaria = faixa_etaria

    #gets de jogo
    def getPlataforma(self):
        return self.__plataforma

    def getFaixa_etaria(self):
        return self.__faixa_etaria

class Clientes:
    def __init__(self, nome:str, cpf:str):
        self.__nome = nome
        self.__cpf = cpf
        self.__itens_Locados = []

    def locar (self, item:Itens):
            item.alugar()
            self.__itens_Locados.append(item)


    def devolver (self, item:Itens):
        if item in self.__itens_Locados:
            item.devolver()
            self.__itens_Locados.remove(item)
            return True
        return False

    def listar_itens (self):
        return self.__itens_Locados
    
    #gets do cliente
    def getCpf(self):
        return self.__cpf

    def getItens_locados(self):
        return self.__itens_locados
    
    def getNome(self):
        return self.__nome
        

class Locadora:
    def __init__ (self):
        self.__clientes = []
        self.__itens = []

    def cadastrar_cliente(self, cliente: Clientes):
        self.__clientes.append(cliente)

    def cadastrar_itens (self, item: Itens):
        self.__itens.append (item)


    def listar_clientes(self):
        print("\nClientes:")
        for cliente in self.__clientes:
            print(f"- {cliente.getNome()} (CPF: {cliente.getCpf()})")
            
    def listar_itens(self):
        print("\nItens:")
        for item in self.__itens:
            status = "Disponível" if item.is_disponivel() else "Alugado"
            print(f"- {item.getCodigo()} - {item.getTitulo()} ({status})")
    
    #gets da locadora
    def getClientes(self):
        return self.__clientes

    def getItens(self):
        return self.__itens
    
    
