"""
Modulo para gerenciamento de pessoas:
REsponsável pelo cadastro e manutenção de Clientes, Fornecedores e Funcionários
Possui funções definidas na especificação

"""
from clientes import *

class Pessoas(object):

    # classe para funcionalidades de clientes, fornecedores e funcionários
    def __init__(self):
        self.clientes = []
        self.fornecedores = []
        self.funcionários = []

    def menu_pessoas(self):
        while True:
            print("||||||| *** Sistema de Vendas ao Consumidor *** |||||||")
            print("****** MENU DE PESSOAS *****")
            print("Digite Ação!\n1 - Consultar Cadastro\n2 - Adicionar\n3 - Remover\n4 - Alterar\n0 - SAIR")
            opcao = input()

            while not self.valida_opcao(opcao):
                print("Opção Inválida!")
                opcao = input()

            if opcao == '1':
                self.consultar()
            elif opcao == '2':
                self.adiciona_item()
            elif opcao == '3':
                self.remove_item()
            elif opcao == '4':
                self.altera_item()
            elif opcao == '0':
                break

    def valida_opcao(self, opcao):
        if opcao.isdigit() and opcao in "01234":
            return True
        else:
            return False

    # metodos pra salvar os objetos em disco
    def save_clientes(self):
        pass

    def save_fornecedores(self):
        pass

    def save_funcionarios(self):
        pass

    # funções pedidas na especificação

    def novo(self):
        pass

    def alterar(self):
        pass

    def remover(self):
        pass

    def consultar(self):
        pass


