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
            data = input("DATA DE NASCIMENTO: ")

        cliente = Cliente(nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro, data)

        if cliente not in self.clientes:
            self.clientes.append(cliente)
            print("\nCliente Cadastrado com SUCESSO!!")

    def novo_funcionario(self):

        cadastro = input("CPF: ")
        while not Pessoa.valida_cadastro(cadastro):
            cadastro = input("CPF: ")
        if len(self.funcionarios):
            for funcionario in self.funcionarios:
                if funcionario.cadastro == cadastro:
                    print("Funcionário já Cadastrado!")
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
        while not Funcionario.valida_data(data):
            data = input("DATA DE NASCIMENTO(dd/mm/aaaa): ")

        funcionario = Funcionario(nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro, data, gerente)

        if funcionario not in self.funcionarios:
            self.funcionarios.append(funcionario)
            print("\nFuncionário Cadastrado com SUCESSO!!")

    def novo_fornecedor(self):
        cadastro = input("CNPJ: ")
        while not Pessoa.valida_cadastro(cadastro):
            cadastro = input("CPF: ")
        if len(self.fornecedores):
            for fornecedor in self.fornecedores:
                if fornecedor.cadastro == cadastro:
                    print("Fornecedor Já Cadastrado!")
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

        fornecedor = Fornecedor(nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, cadastro)

        if fornecedor not in self.fornecedores:
            self.fornecedores.append(fornecedor)
            print("\nFornecedor Cadastrado com SUCESSO!!")

    def alterar(self):
        """
        Alterar: Usado para corrigir campos no objeto passado.
        Se o campo for deixado em branco nada é alterado.

        :return: objeto alterado
        """
        # Alterar copiado da Classe Estoque
        # TODO: Modificar para se adequar aos objetos manipulados por essa classe

        while 1:
            print("Escolha o Item que deseja ALTERAR")
            print("1- Editar Cliente\n2- Editar Fornecedor\n3- Editar Funcionário\n0 - SAIR")
            opcao = input()

            while not self.valida_opcao(opcao, "0123"):
                print("Opção Inválida!")
                opcao = input()

            if opcao == '1':
                if not len(self.clientes):
                    print("Não há Clientes Cadastrados!\n")
                else:
                    print("Escolha um Cliente: ")
                    [print(cliente.cadastro, cliente.nome) for cliente in self.clientes]
                    opcao = input("\nDigite CPF Escolhido: ")
                    while not Cliente.valida_cadastro(opcao):
                        print("Digite CPF Inválido!")
                        opcao = input("\nDigite CPF Escolhido: ")
                    for cliente in self.clientes:
                        if cliente.cadastro == opcao:
                            print("Deixe em branco (PRESS ENTER) para não alterar o campo!")

                            nome = input("\nNOME: ")
                            if nome == "":
                                pass
                            else:
                                while not Cliente.valida_nome(nome):
                                    nome = input("\nNOME: ")
                                else:
                                    cliente.nome = nome

                            end = input("\nENDEREÇO: ")
                            if end == "":
                                pass
                            else:
                                while not Cliente.valida_endereco(end):
                                    end = input("\nENDEREÇO: ")
                                else:
                                    cliente.endereco = end

                            num = input("\nN°: ")
                            if num == "":
                                pass
                            else:
                                while not Cliente.valida_numero(num):
                                    num = input("\nN°: ")
                                else:
                                    cliente.numero = num

                            comp = input("\nCOMPLEMENTO: ")
                            if comp == "":
                                pass
                            else:
                                cliente.complemento = comp

                            bairro = input("BAIRRO: ")
                            if bairro == "":
                                pass
                            else:
                                while not Cliente.valida_bairro(bairro):
                                    bairro = input("\nBAIRRO: ")
                                else:
                                    cliente.bairro = bairro

                            cidade = input("CIDADE: ")
                            if cidade == "":
                                pass
                            else:
                                while not Cliente.valida_cidade(cidade):
                                    cidade = input("\nCIDADE: ")
                                else:
                                    cliente.cidade = cidade

                            cep = input("CEP: ")
                            if cep == "":
                                pass
                            else:
                                while not Cliente.valida_cep(cep):
                                    cep = input("\nCEP: ")
                                else:
                                    cliente.cep = cep

                            uf = input("UF: ")
                            if uf == "":
                                pass
                            else:
                                while not Cliente.valida_estado(uf):
                                    uf = input("\nUF: ")
                                else:
                                    cliente.estado = uf

                            tel = input("TELEFONE: ")
                            if tel == "":
                                pass
                            else:
                                while not Cliente.valida_telefone(tel):
                                    tel = input("\nTELEFONE: ")
                                else:
                                    cliente.telefone = tel

                            cel = input("CELULAR: ")
                            if cel == "":
                                pass
                            else:
                                while not Cliente.valida_celular(cel):
                                    cel = input("\nCELULAR: ")
                                else:
                                    cliente.celular = cel

                            email = input("EMAIL: ")
                            if email == "":
                                pass
                            else:
                                while not Cliente.valida_email(email):
                                    email = input("\nEMAIL: ")
                                else:
                                    cliente.email = email

                            rg = input("RG: ")
                            if rg == "":
                                pass
                            else:
                                while not Cliente.valida_rg(rg):
                                    rg = input("\nRG: ")
                                else:
                                    cliente.rg = rg

                            cpf = input("CPF: ")
                            if cpf == "":
                                pass
                            else:
                                while not Cliente.valida_cadastro(cpf):
                                    cpf = input("\nCPF: ")
                                else:
                                    cliente.cadastro = cpf
                        else:
                            print("Cliente não encontrado!\n")

            elif opcao == '2':
                if not len(self.fornecedores):
                    print("Não há Fornecedores Cadastrados!\n")
                else:
                    print("Escolha um Fornecedor: ")
                    [print(fornecedor.cadastro, fornecedor.nome) for fornecedor in self.fornecedores]
                    opcao = input("\nDigite CNPJ Escolhido: ")
                    while not Fornecedor.valida_cadastro(opcao):
                        print("Digite CNPJ Inválido!")
                        opcao = input("\nDigite CNPJ Escolhido: ")
                    for fornecedor in self.fornecedores:
                        if fornecedor.cadastro == opcao:
                            print("Deixe em branco (PRESS ENTER) para não alterar o campo!")

                            nome = input("\nNOME: ")
                            if nome == "":
                                pass
                            else:
                                while not Forncedor.valida_nome(nome):
                                    nome = input("\nNOME: ")
                                else:
                                    fornecedor.nome = nome

                            end = input("\nENDEREÇO: ")
                            if end == "":
                                pass
                            else:
                                while not Forncedor.valida_endereco(end):
                                    end = input("\nENDEREÇO: ")
                                else:
                                    fornecedor.endereco = end

                            num = input("\nN°: ")
                            if num == "":
                                pass
                            else:
                                while not Forncedor.valida_numero(num):
                                    num = input("\nN°: ")
                                else:
                                    fornecedor.numero = num

                            comp = input("\nCOMPLEMENTO: ")
                            if comp == "":
                                pass
                            else:
                                fornecedor.complemento = comp

                            bairro = input("BAIRRO: ")
                            if bairro == "":
                                pass
                            else:
                                while not Forncedor.valida_bairro(bairro):
                                    bairro = input("\nBAIRRO: ")
                                else:
                                    fornecedor.bairro = bairro

                            cidade = input("CIDADE: ")
                            if cidade == "":
                                pass
                            else:
                                while not Forncedor.valida_cidade(cidade):
                                    cidade = input("\nCIDADE: ")
                                else:
                                    fornecedor.cidade = cidade

                            cep = input("CEP: ")
                            if cep == "":
                                pass
                            else:
                                while not Forncedor.valida_cep(cep):
                                    cep = input("\nCEP: ")
                                else:
                                    fornecedor.cep = cep

                            uf = input("UF: ")
                            if uf == "":
                                pass
                            else:
                                while not Forncedor.valida_estado(uf):
                                    uf = input("\nUF: ")
                                else:
                                    fornecedor.estado = uf

                            tel = input("TELEFONE: ")
                            if tel == "":
                                pass
                            else:
                                while not Forncedor.valida_telefone(tel):
                                    tel = input("\nTELEFONE: ")
                                else:
                                    fornecedor.telefone = tel

                            cel = input("CELULAR: ")
                            if cel == "":
                                pass
                            else:
                                while not Forncedor.valida_celular(cel):
                                    cel = input("\nCELULAR: ")
                                else:
                                    fornecedor.celular = cel

                            email = input("EMAIL: ")
                            if email == "":
                                pass
                            else:
                                while not Forncedor.valida_email(email):
                                    email = input("\nEMAIL: ")
                                else:
                                    fornecedor.email = email

                            rg = input("RG: ")
                            if rg == "":
                                pass
                            else:
                                while not Forncedor.valida_rg(rg):
                                    rg = input("\nRG: ")
                                else:
                                    fornecedor.rg = rg

                            cpf = input("CNPJ: ")
                            if cpf == "":
                                pass
                            else:
                                while not Forncedor.valida_cadastro(cpf):
                                    cpf = input("\nCNPJ: ")
                                else:
                                    fornecedor.cadastro = cpf
                        else:
                            print("Fornecedor não encontrado!\n")

            elif opcao == '3':

                if not len(self.funcionarios):
                    print("Não há Funcionários Cadastrados!\n")
                else:
                    print("Escolha um Funcionário: ")
                    [print(funcionario.cadastro, funcionario.nome) for funcionario in self.funcionarios]
                    opcao = input("\nDigite CPF Escolhido: ")
                    while not Funcionario.valida_cadastro(opcao):
                        print("Digite CPF Inválido!")
                        opcao = input("\nDigite CPF Escolhido: ")
                    for funcionario in self.funcionarios:
                        if funcionario.cadastro == opcao:
                            print("Deixe em branco (PRESS ENTER) para não alterar o campo!")

                            nome = input("\nNOME: ")
                            if nome == "":
                                pass
                            else:
                                while not Funcionario.valida_nome(nome):
                                    nome = input("\nNOME: ")
                                else:
                                    funcionario.nome = nome

                            end = input("\nENDEREÇO: ")
                            if end == "":
                                pass
                            else:
                                while not Funcionario.valida_endereco(end):
                                    end = input("\nENDEREÇO: ")
                                else:
                                    funcionario.endereco = end

                            num = input("\nN°: ")
                            if num == "":
                                pass
                            else:
                                while not Funcionario.valida_numero(num):
                                    num = input("\nN°: ")
                                else:
                                    funcionario.numero = num

                            comp = input("\nCOMPLEMENTO: ")
                            if comp == "":
                                pass
                            else:
                                funcionario.complemento = comp

                            bairro = input("BAIRRO: ")
                            if bairro == "":
                                pass
                            else:
                                while not Funcionario.valida_bairro(bairro):
                                    bairro = input("\nBAIRRO: ")
                                else:
                                    funcionario.bairro = bairro

                            cidade = input("CIDADE: ")
                            if cidade == "":
                                pass
                            else:
                                while not Funcionario.valida_cidade(cidade):
                                    cidade = input("\nCIDADE: ")
                                else:
                                    funcionario.cidade = cidade

                            cep = input("CEP: ")
                            if cep == "":
                                pass
                            else:
                                while not Funcionario.valida_cep(cep):
                                    cep = input("\nCEP: ")
                                else:
                                    funcionario.cep = cep

                            uf = input("UF: ")
                            if uf == "":
                                pass
                            else:
                                while not Funcionario.valida_estado(uf):
                                    uf = input("\nUF: ")
                                else:
                                    funcionario.estado = uf

                            tel = input("TELEFONE: ")
                            if tel == "":
                                pass
                            else:
                                while not Funcionario.valida_telefone(tel):
                                    tel = input("\nTELEFONE: ")
                                else:
                                    funcionario.telefone = tel

                            cel = input("CELULAR: ")
                            if cel == "":
                                pass
                            else:
                                while not Funcionario.valida_celular(cel):
                                    cel = input("\nCELULAR: ")
                                else:
                                    funcionario.celular = cel

                            email = input("EMAIL: ")
                            if email == "":
                                pass
                            else:
                                while not Funcionario.valida_email(email):
                                    email = input("\nEMAIL: ")
                                else:
                                    funcionario.email = email

                            rg = input("RG: ")
                            if rg == "":
                                pass
                            else:
                                while not Funcionario.valida_rg(rg):
                                    rg = input("\nRG: ")
                                else:
                                    funcionario.rg = rg

                            cpf = input("CPF: ")
                            if cpf == "":
                                pass
                            else:
                                while not Funcionario.valida_cadastro(cpf):
                                    cpf = input("\nCPF: ")
                                else:
                                    funcionario.cadastro = cpf
                        else:
                            print("Funcionário não encontrado!\n")

            elif opcao == '0':
                break

    def remover(self):
        """
                Escolhe um tipo de item a ser removido do sistema de Pessoas
                Apos escolhido o objeto, é chamado o metodo del daquele objeto e então é destruido e removido da lista
                de objetos

                Se o item escolhido já tiver sido negociado não pode ser removido

                :return: Sucess - "Item Removido com Sucesso!" or Fail - "Item não pode ser removido!"
                """

        print("Removendo Pessoa")

        while 1:
            print("Digite o tipo de ITEM que deseja remover:\n1- Cliente\n2- Fornecedor\n3- Funcionário\n0- SAIR")

            opcao = input()

            while not self.valida_opcao(opcao, "0123"):
                print("Opção Inválida!")
                opcao = input()

            if opcao == '1':
                if not len(self.clientes):
                    print("Não há Clientes Registrados!\n")
                else:
                    print("Escolha Cliente: ")
                    [print(cliente.cadastro, cliente.nome) for cliente in self.clientes]
                    opcao = input("\nDigite CPF Escolhido: ")
                    for cliente in self.clientes:
                        if cliente.cadastro == opcao:
                            index = self.clientes.index(cliente)
                            del self.clientes[index]
                            break
                        else:
                            print("Cliente não encontrado!\n")

            elif opcao == '2':
                if not len(self.fornecedores):
                    print("Não há Fornecedores Registrados!\n")
                else:
                    print("Escolha um Forncedor: ")
                    [print(fornecedor.cadastro, fornecedor.nome) for fornecedor in self.fornecedores]
                    opcao = input("\nDigite CNPJ Escolhido: ")
                    for fornecedor in self.fornecedores:
                        if fornecedor.cadastro == opcao:
                            index = self.fornecedores.index(fornecedor)
                            del self.fornecedores[index]
                            break
                        else:
                            print("Fornecedor não encontrado!\n")

            elif opcao == '3':
                if not len(self.funcionarios):
                    print("Não há Funcionários Registrados!\n")
                else:
                    print("Escolha um Funcionário: ")
                    [print(funcionario.codigo, funcionario.nome) for funcionario in self.funcionarios]
                    opcao = input("\nDigite Código Escolhido: ")
                    for funcionario in self.funcionarios:
                        if funcionario.cadastro == opcao:
                            index = self.funcionarios.index(funcionario)
                            del self.funcionarios[index]
                            break
                        else:
                            print("Funcionário não encontrado!\n")

            elif opcao == '0':
                break

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
