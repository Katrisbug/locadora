from funcoes import *
from classes import *


while True:
        try:
            print("\n--------- LOCADORA ---------")
            print("1 - Cadastrar cliente")
            print("2 - Cadastrar item")
            print("3 - Listar clientes")
            print("4 - Listar itens")
            print("5 - Locar item")
            print("6 - Devolver item")
            print("0 - Sair")

            opcao = input("\n --> ")

            match opcao:
                case "1":
                    ls()
                    cadastrar_cliente(locadora)
                    ls()
                case "2":
                    ls()
                    cadastrarItem(locadora)
                    ls()
                case "3":
                    ls()
                    listar_clientes(locadora)
                    ls()
                case "4":
                    ls()
                    listar_itens(locadora)
                    ls()
                case "5":
                    ls()
                    locar_item(locadora)
                    ls()
                case "6":
                    ls()
                    devolver_item(locadora)
                    ls()
                case "0":
                    ls()
                    print("Saindo...")
                    break
                case _:
                    print("Opção inválida!")

        except Exception as e:
            print(f"Erro: {e}")