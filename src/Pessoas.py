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
        self.funcionarios = []

    def menu_pessoas(self):
        while True:
            print("||||||| *** Sistema de Vendas ao Consumidor *** |||||||")
            print("****** MENU DE PESSOAS *****")
            print("Digite Ação!\n1 - Consultar Cadastro\n2 - Adicionar\n3 - Remover\n4 - Alterar\n0 - SAIR")
            opcao = input()

            while not self.valida_opcao(opcao, "01234"):
                print("Opção Inválida!")
                opcao = input()

            if opcao == '1':
                self.consultar()
            elif opcao == '2':
                self.novo()
            elif opcao == '3':
                self.remover()
            elif opcao == '4':
                self.alterar()
            elif opcao == '0':
                break

    def valida_opcao(self, opcao, oplist):
        if opcao.isdigit() and opcao in oplist:
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
        while True:
            print("||||||| *** Sistema de Vendas ao Consumidor *** |||||||")
            print("****** CRIAR NOVO *****")
            print("Digite Ação!\n1 - Novo Cliente\n2 - Novo Funcionário \n3 - Novo Fornecedor\n0 - SAIR")
            opcao = input()

            while not self.valida_opcao(opcao, "0123"):
                print("Opção Inválida!")
                opcao = input()

            if opcao == '1':
                self.novo_cliente()
            elif opcao == '2':
                self.novo_funcionario()
            elif opcao == '3':
                self.novo_fornecedor()
            elif opcao == '4':
                self.alterar()
            elif opcao == '0':
                break

    def novo_cliente(self):

        cadastro = input("CPF: ")
        while not Pessoa.valida_cadastro(cadastro):
            cadastro = input("CPF: ")
        if len(self.clientes):
            for cliente in self.clientes:
                if cliente.cadastro == cadastro:
                    print("Cliente Já Cadastrado!")
                    return 0

        nome = input("NOME COMPLETO: ")
        while not Pessoa.valida_nome(nome):
            nome = input("NOME COMPLETO: ")

        end = input("ENDEREÇO: ")
        while not Pessoa.valida_endereco(end):
            end = input("ENDEREÇO: ")

        num = input("Nº: ")
        while not Pessoa.valida_numero(num):
            num = input("Nº: ")

        complemento = input("COMPLEMENTO: ")                                      # Complemento não necessita validação?

        bairro = input("BAIRRO: ")
        while not Pessoa.valida_bairro(bairro):
            bairro = input("BAIRRO: ")

        cidade = input("CIDADE: ")
        while not Pessoa.valida_cidade(cidade):
            cidade = input("CIDADE: ")

        cep = input("CEP: ")
        while not Pessoa.valida_cep(cep):
            cep = input("CEP: ")

        uf = input("UF: ")
        while not Pessoa.valida_estado(uf):
            uf = input("UF: ")

        tel = input("TELEFONE: ")
        while not Pessoa.valida_telefone(tel):
            tel = input("TELEFONE: ")

        cel = input("CELULAR: ")
        while not Pessoa.valida_celular(cel):
            cel = input("CELULAR: ")

        email = input("EMAIL: ")
        while not Pessoa.valida_email(email):
            email = input("EMAIL: ")

        rg = input("RG: ")
        while not Pessoa.valida_rg(rg):
            rg = input("RG: ")

        data = input("DATA DE NASCIMENTO(dd/mm/aaaa): ")
        while not Cliente.valida_data(data):
            end = input("DATA DE NASCIMENTO: ")

        cliente = Cliente(nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro, data)

        if cliente not in self.clientes:
            self.clientes.append(cliente)
            print("\nCliente Cadastrado com SUCESSO!!")

    def novo_funcionario(self):

        cadastro = input("CPF: ")
        while not Pessoa.valida_cadastro(cadastro):
            cadastro = input("CPF: ")
        if len(self.clientes):
            for cliente in self.clientes:
                if cliente.cadastro == cadastro:
                    print("Funcionário Já Cadastrado!")
                    return 0
        gerente = input("Gerente(S/N): ")
        while not Funcionario.valida_status(gerente):
            gerente = input("Gerente(S/N): ")

        nome = input("NOME COMPLETO: ")
        while not Pessoa.valida_nome(nome):
            nome = input("NOME COMPLETO: ")

        end = input("ENDEREÇO: ")
        while not Pessoa.valida_endereco(end):
            end = input("ENDEREÇO: ")

        num = input("Nº: ")
        while not Pessoa.valida_numero(num):
            end = input("Nº: ")

        complemento = input("COMPLEMENTO: ")                                      # Complemento não necessita validação?

        bairro = input("BAIRRO: ")
        while not Pessoa.valida_bairro(bairro):
            end = input("BAIRRO: ")

        cidade = input("CIDADE: ")
        while not Pessoa.valida_cidade(cidade):
            end = input("CIDADE: ")

        cep = input("CEP: ")
        while not Pessoa.valida_cep(cep):
            end = input("CEP: ")

        uf = input("UF: ")
        while not Pessoa.valida_estado(uf):
            uf = input("UF: ")

        tel = input("TELEFONE: ")
        while not Pessoa.valida_telefone(tel):
            end = input("TELEFONE: ")

        cel = input("CELULAR: ")
        while not Pessoa.valida_celular(cel):
            end = input("CELULAR: ")

        email = input("EMAIL: ")
        while not Pessoa.valida_email(email):
            end = input("EMAIL: ")

        rg = input("RG: ")
        while not Pessoa.valida_rg(rg):
            end = input("RG: ")

        data = input("DATA DE NASCIMENTO(dd/mm/aaaa): ")
        while not Funcionario.valida_data(data):
            data = input("DATA DE NASCIMENTO: ")

        funcionario = Funcionario(nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro, data, gerente)

        if funcionario not in self.funcionarios:
            self.funcionarios.append(funcionario)
            print("\nFuncionário Cadastrado com SUCESSO!!")

    def novo_fornecedor(self):
        def novo_cliente(self):

            cadastro = input("CPF: ")
            while not Pessoa.valida_cadastro(cadastro):
                cadastro = input("CPF: ")
            if len(self.clientes):
                for cliente in self.clientes:
                    if cliente.cadastro == cadastro:
                        print("Cliente Já Cadastrado!")
                        return 0

            nome = input("NOME COMPLETO: ")
            while not Pessoa.valida_nome(nome):
                nome = input("NOME COMPLETO: ")

            end = input("ENDEREÇO: ")
            while not Pessoa.valida_endereco(end):
                end = input("ENDEREÇO: ")

            num = input("Nº: ")
            while not Pessoa.valida_numero(num):
                num = input("Nº: ")

            complemento = input("COMPLEMENTO: ")  # Complemento não necessita validação?

            bairro = input("BAIRRO: ")
            while not Pessoa.valida_bairro(bairro):
                bairro = input("BAIRRO: ")

            cidade = input("CIDADE: ")
            while not Pessoa.valida_cidade(cidade):
                cidade = input("CIDADE: ")

            cep = input("CEP: ")
            while not Pessoa.valida_cep(cep):
                cep = input("CEP: ")

            uf = input("UF: ")
            while not Pessoa.valida_estado(uf):
                uf = input("UF: ")

            tel = input("TELEFONE: ")
            while not Pessoa.valida_telefone(tel):
                tel = input("TELEFONE: ")

            cel = input("CELULAR: ")
            while not Pessoa.valida_celular(cel):
                cel = input("CELULAR: ")

            email = input("EMAIL: ")
            while not Pessoa.valida_email(email):
                email = input("EMAIL: ")

            fornecedor = Forcedor(nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, cadastro)

            if fornecedor not in self.fornecedores:
                self.fornecedores.append(fornecedor)
                print("\nFornecedor Cadastrado com SUCESSO!!")

    def alterar(self):
        pass

    def remover(self):
        pass

    def consultar(self):
        """"
        Metodo Consultar (Pessoas): Exibe na tela os itens que estão registrados
        Retorna se houver:
                    >Lista de clientes
                    >Lista de funcionários
                    >Lista de fornecedores
                """
        # TODO : Uma forma melhor de exibir na tela as informações
        print("Exibindo PESSOAS\n")
        if not len(self.clientes):
            print("Não há Clientes Registrados!\n")
        else:
            print("CLIENTES CADASTRADOS")
            print("CPF\t\t\tNOME:\t\t\t\tTELEFONE\t\tEMAIL")
            for cliente in self.clientes:
                print(cliente.cadastro, cliente.nome, cliente.telefone, cliente.email)

        if not len(self.funcionarios):
            print("\nNão há Funcionários Registrados!\n")
        else:
            print("FUNCIONÁRIOS CADASTRADOS")
            print("CPF\t\tNOME:\t\t\t\tTELEFONE\t\tEMAIL")
            for funcionario in self.funcionarios:
                print(funcionario.cadastro, funcionario.nome, funcionario.telefone, funcionario.email)

        if not len(self.fornecedores):
            print("Não há Fornecedores Registrados!\n")
        else:
            print("<h1>FORNECEDORES CADASTRADOS</h1>")
            print("CNPJ\t\tNOME:\t\t\t\tTELEFONE\t\tEMAIL")
            for forncedor in self.fornecedores:
                print(forncedor.cadastro, forncedor.nome, forncedor.telefone, forncedor.email)

p = Pessoas()
p.menu_pessoas()
