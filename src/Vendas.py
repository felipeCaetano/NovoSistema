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
    resumodecompras = []

    def __init__(self):
        self.vendidos = []
        self.comprados = []

    def menu_vendas(self, estoque, pessoas):
        while True:
            print(chr(847)*25, "- Sistema de Vendas ao Consumidor -", chr(847)*25)
            print(chr(847)*25, "- MENU DE VENDAS -", chr(847)*25)
            print("Escolha:\n1- Iniciar Venda\n2- Iniciar Compra\n3- Relatorio de Vendas\n"
                  "4- Relatorio de Compras\n0- SAIR")

            opcao = input()
            while not self.valida_opcao(opcao):
                print("Opção Inválida!")
                opcao = input()
            opcao = int(opcao)

            if opcao == 1:
                self.vender(estoque, pessoas)
            elif opcao == 2:
                self.comprar(estoque, pessoas)
            elif opcao == 3:
                self.relatorio_venda()
            elif opcao == 4:
                self.relatorio_compra()
            elif opcao == 0:
                break

    def valida_opcao(self, opcao):
        if opcao.isdigit() and opcao in "01234":
            return True
        else:
            return False

    def vender(self, e, p):
        '''
        digite cpf ou nome do cliente para inciar a venda
        caso seja digitado o nome: o sistema deve recuperar o cpf da lista de clientes com o mesmo nome
        :param e: objeto estoque
        :param p: objeto pessoas
        :return: none
        '''

        listadecompras = []
        total = 0

        novavenda = True
        if not len(e.produtos) or not len(p.clientes):
            print("Lista de Produtos ou Clientes Vazia! Necessita cadastrar\n")
            return 0
        else:
            print(chr(847)*80)
            print(chr(847), end="")
            cpf = input("Digite CPF do Cliente: ")
            if cpf:
                while not funcionalidades.valida_cadastro(cpf):
                    print(chr(847), end="")
                    cpf = input("Digite CPF do Cliente: ")
                cpf = funcionalidades.remove_caracter(cpf)
            else:
                nome = input("Digite Nome do Cliente: ")

            for cliente in p.clientes:
                cliente.cadastro = funcionalidades.remove_caracter(cliente.cadastro)
                if cliente.cadastro == cpf:
                    print("Vendendo para: %s\n" % cliente.nome)
                    while novavenda:
                        print(chr(847), end="")
                        prod = input("Digite o CÓDIGO do produto: ")
                        for produto in e.produtos:
                            if produto.codigo == prod:
                                print(produto.nome, produto.quantidade)
                                print(chr(847), end="")
                                quant = input("Digite a quantidade: ")
                                while not Produtos.valida_estoque(quant):
                                    print(chr(847), end="")
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
                        e.save_produtos()
                        cliente.ativo = True
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
            return True
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
            print(chr(847), end="")
            cpf = input(" Digite CNPJ do Fornecedor: ")
            while not Pessoa.valida_cadastro(cpf):
                print(chr(847), end="")
                cpf = input(" Digite CNPJ do Fornecedor: ")
            for fornecedor in p.fornecedores:
                if fornecedor.cadastro == cpf:
                    print("Comprando de: %s\n" % fornecedor.nome)
                    while novavenda:
                        print(chr(847), end="")
                        prod = input(" Digite o CÓDIGO do produto: ")
                        for produto in e.produtos:
                            if produto.codigo == prod:  # se produto cadastrado
                                print(chr(847), end="")
                                quant = input(" Digite a quantidade: ")
                                while not Produtos.valida_estoque(quant):
                                    print(chr(847), end="")
                                    quant = input(" Digite a quantidade: ")
                                if int(quant) + produto.quantidade > produto.estoquemax:  # Se quantidade maior que capacidade de estoque
                                    print("\nATENÇÃO! Quantidade excede limite MÁXIMO para estoque.\n")
                                    print("Limite: %d\t\tQuantidade Atual: %d" % (produto.estoquemax, produto.quantidade))
                                elif int(quant) + produto.quantidade < produto.estoquemin:
                                    print("\nATENÇÃO! Quantidade final menor que limite MÍNIMO para estoque.\n")
                                    print("Limite: %d\t\tQuantidade Atual: %d"  % (produto.estoquemin, produto.quantidade))
                                op = input("Deseja continuar(S/N): ")
                                while not self.valida_yesorno(op):
                                    op = input("Deseja continuar(S/N): ")
                                if op.lower() == 's' or op.lower() == 'sim':
                                    quant = int(quant)
                                else:
                                    print(chr(847), end="")
                                    quant = input(" Digite a quantidade: ")
                                    while not Produtos.valida_estoque(quant):
                                        print(chr(847), end="")
                                        quant = input(" Digite a quantidade: ")
                                        # TODO: Criar uma fumção para verificar se a entrada está acima ou abaixo do limite
                                    quant = int(quant)
                                print(chr(847), end="")
                                valor = input(" Digite o preço para compra: ")
                                while not Produtos.valida_valorvenda(valor):
                                    print(chr(847), end="")
                                    valor = input(" Digite o preço para compra: ")
                                valor = float(valor)
                                if valor > produto.vbcompra:  # se valor do forncedor for maior q o valor pagavel
                                    print("\nATENÇÃO! Valor alto para compra.\n")
                                    op = input("Deseja continuar(S/N): ")
                                    while not self.valida_yesorno(op):
                                        op = input("Deseja continuar(S/N): ")
                                    if op.lower() == 's' or op.lower() == 'sim':
                                        preco = quant * valor
                                        total += preco
                                        listadecompras.append([produto.codigo, produto.nome, quant, preco])
                                        # TODO: Criar uma função para gerar uma saida padrão (cupom)
                                        for item in listadecompras:
                                            print("%s: %s %d valor: R$ %.2f\n" % (item[0], item[1], item[2], item[3]))
                                            print("TOTAL: R$%.2f" % total)
                                            op = input("\nNovo Item? (S/N): ")
                                            while not self.valida_yesorno(op):
                                                op = input("\nNovo Item? (S/N): ")
                                            if op.lower() == 's' or op.lower() == 'sim':
                                                novavenda = True
                                            else:
                                                novavenda = False
                                    # Danado é essa linha de baixo??
                                    elif op.lower() == 'n' or op.lower() == 'nao' or op.lower() == 'não':
                                       print("\nATENÇÃO! Venda Cancelada.\n")
                                       return  2
                                else:
                                    preco = quant * valor
                                    total += preco
                                    listadecompras.append([produto.codigo, produto.nome, quant, preco])
                                    for item in listadecompras:
                                        print("%s: %s %d valor: R$ %.2f\n" % (item[0], item[1], item[2], item[3]))
                                        print("TOTAL: R$%.2f" % total)
                                        op = input("Novo Item? (S/N): ")
                                        novavenda = self.valida_yesorno(op)
                                break
                            else:
                                print("Quantidade Insuficiente em Estoque! Impossível Vender")
                                return 0
                        else:
                            print("Produto Não Cadastrado!")

                    op = input("Efetuar Pagamento? (S/N): ")
                    while not self.valida_yesorno(op):
                        op = input("\nNovo Item? (S/N): ")
                    if op.lower() == 's' or op.lower() == 'sim':
                        op = True
                    else:
                        op = False
                    #choice = self.valida_yesorno(op)
                    if op:
                        self.pagamento(total, listadecompras, fornecedor)
                        produto.quantidade += quant
                        e.save_produtos()
                        break
                    else:
                        print("\nATENÇÃO! Venda Cancelada.\n")
                        return 1
            else:
                print("\nForncedor Não Cadastrado! Cadastrar? (S/N)")
                op = input()
                while not self.valida_yesorno(op):
                    op = input("\nCadastrar? (S/N)")
                if op.lower() == 's' or op.lower() == 'sim':
                    p.novo_fornecedor()
                else:
                    return 0

    def relatorio_venda(self):
        print("Cadastro:\t\t\tNome:\t\t\t\n")
        for item in self.resumodevendas:
            print("%s\t\t\t%s\t\t\t\n" % (item[0].cadastro, item[0].nome))
            print("Itens Adquiridos:")
            print("Codigo\tNome\t\tQuantidade\tValor")
            for compras in item[1]:
                print("%s\t%s\t\t%s\t%s" % (compras[0], compras[1], compras[2], compras[3]))
            print("Total:", end='')
            print(item[2])
            print("Dinheiro: R$ %s\tTroco: %s" % (item[3], item[4]))

    def relatorio_compra(self):
        print("Cadastro:\t\t\tNome:\t\t\t\n")
        for item in self.resumodecompras:
            print("%s\t\t\t%s\t\t\t\n" % (item[0].cadastro, item[0].nome))
            print("Itens Adquiridos:")
            print("Codigo\tNome\t\tQuantidade\tValor")
            for compras in item[1]:
                print("%s\t%s\t\t%s\t%s" % (compras[0], compras[1], compras[2], compras[3]))
            print("Total:", end='')
            print(item[2])
            print("Dinheiro: R$ %s\tTroco: %s" % (item[3], item[4]))

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
                if type(pessoa) == Cliente:
                    self.resumodevendas.append([pessoa, listadecompras, total, dinheiro, troco])
                elif type(pessoa) == Fornecedor:
                    self.resumodecompras.append([pessoa, listadecompras, total, dinheiro, troco])
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

'''
if __name__ != "__main__":
    e = Estoque()
    p = Pessoas()
    v = Vendas()
   # v.menu_vendas()
'''
