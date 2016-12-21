"""
Modulo de Vendas:
Modulo responsável pelo controle de compra/vendas dos produtos

Para vendas:
    Necessario Clientes cadastrados
    Necessario Funcionário Logado
    NEcessario Produto cadastrado

    Para vendas:
    Funcionario - digita codigo do produto e quantidade a ser vendida. Se houver quantidade disponível no estoque
    sistema calcula preco, perguntado se haverá novos itens e processo se repete
    se não houver itens finaliza venda, recebe dinheiro e passa troco

    PAra comprar:
    Funcionario com acesso de gerente digita codigo de produto e seleciona fornecedor. Sistema calcula quantidade
    e preço e finaliza venda

    Modulo de vendas também gera relatório de compra/venda
"""

from Estoque import *
from Pessoas import *


class Vendas(object):
    resumodevendas = []

    def __init__(self):
        self.vendidos = []
        self.comprados = []

    def menu_vendas(self):
        while True:
            print("Sistema de Vendas ao Consumidor")
            print("****** MENU DE VENDAS *****")
            print("Escolha:\n1- Iniciar Venda\n2- Iniciar Compra\n3- Relatorio de Vendas\n"
                  "4- Relatorio de Compras\n0- SAIR")
            opcao = input()

            while not self.valida_opcao(opcao):
                print("Opção Inválida!")
                opcao = input()

            if opcao == '1':
                self.vender(e, p)
            elif opcao == '2':
                self.comprar(e, p)
            elif opcao == '3':
                self.relatorio_venda()
            elif opcao == '4':
                self.relatorio_compra()
            elif opcao == '0':
                break

    def valida_opcao(self, opcao):
        if opcao.isdigit() and opcao in "01234":
            return True
        else:
            return False

    def vender(self, e, p):

        listadecompras = []
        total = 0

        novavenda = True
        if not len(e.produtos) or not len(p.clientes):
            print("Lista de Produtos ou Clientes Vazia! Necessita cadastrar\n")
            return 0
        else:
            cpf = input("Digite CPF do Cliente: ")
            while not Pessoa.valida_cadastro(cpf):
                cpf = input("Digite CPF do Cliente: ")
            for cliente in p.clientes:
                if cliente.cadastro == cpf:
                    print("Vendendo para: %s\n" % cliente.nome)
                    while novavenda:
                        prod = input("Digite o CÓDIGO do produto: ")
                        for produto in e.produtos:
                            if produto.codigo == prod:

                                print(produto.nome, produto.quantidade)

                                quant = input("Digite a quantidade: ")
                                while not Produtos.valida_estoque(quant):
                                    quant = input("Digite a quantidade: ")
                                quant = int(quant)
                                if quant <= produto.quantidade:
                                    produto.quantidade -= quant
                                    preco = quant * produto.vbvenda
                                    total += preco
                                    listadecompras.append([produto.codigo, produto.nome, quant, preco])
                                    for item in listadecompras:
                                        print("%s: %s %d valor: R$ %.2f\n" % (item[0], item[1], item[2], item[3]))
                                    print("TOTAL: %.2f" % total)
                                    op = input("Novo Item? (S/N): ")
                                    novavenda = self.valida_yesorno(op)
                                else:
                                    print("Quantidade Insuficiente em Estoque! Impossível Vender")
                                    return 0
                            else:
                                print("Produto Não Cadastrado!")

                    op = input("Efetuar Pagamento? (S/N): ")
                    choice = self.valida_yesorno(op)
                    if choice:
                        self.pagamento(total, listadecompras, cliente)
                        break
                    else:
                        print("Venda Cancelada!")
                        return 1
            else:
                print("Cliente Não Cadastrado! Cadastrar? (S/N)")
                op = input()
                if self.valida_yesorno(op):
                    p.novo_cliente()
                else:
                    return 0

    def valida_yesorno(self, op):
        if op.lower() == 'n' or op.lower() == 'não' or op.lower() == 'nao':
            return False
        elif op.lower() == 's' or op.lower() == 'sim':
            return True
        else:
            print("opção inválida")
            return False

    def comprar(self, e, p):
        listadecompras = []
        total = 0
        novavenda = True

        if not len(e.produtos) or not len(p.fornecedores):
            print("Lista de Produtos ou Forncedores Vazia! Necessita cadastrar\n")
            return 0
        else:
            cpf = input("Digite CNPJ do Fornecedor: ")
            while not Pessoa.valida_cadastro(cpf):
                cpf = input("Digite CNPJ do Fornecedor: ")
            for fornecedor in p.fornecedores:
                if fornecedor.cadastro == cpf:
                    print("Comprando de: %s\n" % fornecedor.nome)
                    while novavenda:
                        prod = input("Digite o CÓDIGO do produto: ")
                        for produto in e.produtos:
                            if produto.codigo == prod:  # se produto cadastrado
                                quant = input("Digite a quantidade: ")
                                while not Produtos.valida_estoque(quant):
                                    quant = input("Digite a quantidade: ")
                                quant = int(quant)
                                if quant > produto.estoquemax:  # Se quantidade maior que capacidade de estoque
                                    print("Quantidade excede limite para estoque!\n")
                                elif quant <= produto.estoquemax:
                                    valor = input("Digite o preço para compra: ")
                                    while not Produtos.valida_valorvenda(valor):
                                        valor = input("Digite o preço para compra: ")
                                    valor = float(valor)
                                    if valor > produto.vbcompra:  # se valor do forncedor for maior q o valor pagavel
                                        print("Valor alto para compra!")
                                        op = input("Deseja continuar(S/N): ")
                                        while self.valida_yesorno(op):
                                            op = input("Deseja continuar(S/N): ")
                                        if op.lower() == 's' or op.lower() == 'sim':
                                            preco = quant * valor
                                            total += preco
                                            listadecompras.append([produto.codigo, produto.nome, quant, preco])
                                            for item in listadecompras:
                                                print(
                                                    "%s: %s %d valor: R$ %.2f\n" % (item[0], item[1], item[2], item[3]))
                                                print("TOTAL: R$%.2f" % total)
                                                op = input("Novo Item? (S/N): ")
                                                novavenda = self.valida_yesorno(op)
                                        elif op.lower() == 'n' or op.lower() == 'nao' or op.lower() == 'não':
                                            return 1
                                    else:
                                        preco = quant * valor
                                        total += preco
                                        listadecompras.append([produto.codigo, produto.nome, quant, preco])
                                        for item in listadecompras:
                                            print("%s: %s %d valor: R$ %.2f\n" % (item[0], item[1], item[2], item[3]))
                                            print("TOTAL: R$%.2f" % total)
                                            op = input("Novo Item? (S/N): ")
                                            novavenda = self.valida_yesorno(op)
                                else:
                                    print("Quantidade Insuficiente em Estoque! Impossível Vender")
                                    return 0
                            else:
                                print("Produto Não Cadastrado!")

                    op = input("Efetuar Pagamento? (S/N): ")
                    choice = self.valida_yesorno(op)
                    if choice:
                        self.pagamento(total, listadecompras, fornecedor)
                        break
                    else:
                        print("Venda Cancelada!")
                        return 1
            else:
                print("Forncedor Não Cadastrado! Cadastrar? (S/N)")
                op = input()
                if self.valida_yesorno(op):
                    p.novo_fornecedor()
                else:
                    return 0

    def relatorio_venda(self):
        pass

    def relatorio_compra(self):
        pass

    def pagamento(self, total, listadecompras, pessoa):
        if type(pessoa) == Cliente:
            print("Finalizando Venda:\n Cliente: %s\tCPF: %s\nItens Adquiridos:\n" % (pessoa.nome, pessoa.cadastro))
        elif type(pessoa) == Fornecedor:
            print("Finalizando Venda:\n Forncedor: %s\tCNPJ: %s\nItens Adquiridos:\n" % (pessoa.nome, pessoa.cadastro))
        for item in listadecompras:
            print("%s: %s %d valor: %d\n" % (item[0], item[1], item[2], item[3]))
        print("TOTAL: %.2f" % total)
        op = input("Confirmar Pagamento? (S/N): ")
        choice = self.valida_yesorno(op)
        if choice:
            print("REALIZANDO PAGAMENTO:\n")
            dinheiro = input("Dinheiro: ")
            troco = self.verifica_pagamento(total, dinheiro)
            if troco < 0:
                self.pagamento(total, listadecompras, pessoa)
            else:
                print("Pagamento Realizado com Sucesso!\n")
                print("Troco: %.2f" % troco)
                print("\nOBRIGADO E VOLTE SEMPRE!!")
                self.resumodevendas.append([pessoa, listadecompras, total, dinheiro, troco])

        else:
            print("Venda Cancelada!")
            return 1

    def verifica_pagamento(self, total, dinheiro):
        dinheiro = dinheiro.replace(",", ".")
        try:
            dinheiro = float(dinheiro)
        except ValueError:
            print("Informe valor numérico!\n")
            return -1

        if dinheiro < total:
            print("Pagamento Insuficiente!\n")
            return -1
        else:
            return dinheiro - total


e = Estoque()
p = Pessoas()
v = Vendas()
v.menu_vendas()
