import os
import funcionalidades
from produtos import *
import pickle


class Estoque(object):
    def __init__(self):
        self.categorias = []
        self.subcategorias = []
        self.produtos = []
        self.load()
        # self.menu_estoque()

    def load(self):
        try:
            with open('categorias.vdc', 'rb') as arquivo_categorias:
                self.categorias = pickle.load(arquivo_categorias)
        except FileNotFoundError:
            self.categorias = []
        try:
            with open('subcategorias.vdc', 'rb') as arquivo_subcategorias:
                self.subcategorias = pickle.load(arquivo_subcategorias)
        except FileNotFoundError:
            self.subcategorias = []
        try:
            with open('produtos.vdc', 'rb') as arquivo_produtos:
                self.produtos = pickle.load(arquivo_produtos)
        except FileNotFoundError:
            self.produtos = []

    def save_categoria(self):
        with open('categorias.vdc', 'wb') as arquivo_categorias:
            pickle.dump(self.categorias, arquivo_categorias)

    def save_subcategorias(self):
        with open('subcategorias.vdc', 'wb') as arquivo_subcategorias:
            pickle.dump(self.subcategorias, arquivo_subcategorias)

    def save_produtos(self):
        with open('produtos.vdc', 'wb') as arquivo_produtos:
            pickle.dump(self.produtos, arquivo_produtos)
        self.low_stock_alarm()

    def create_categoria(self):
        """"
        Cria uma categoria através dos dados recolhidos pelo formulário.
        Os dados são: Codigo, nome e descrição
        """
        print(chr(164)*71)
        print(chr(164)*25, "- CRIAR CATEGORIA -", chr(164)*25)
        print(chr(164) * 71)
        print("\n", chr(164), " ", end="")
        codigo = input("CÓDIGO: ").strip()
        print("\n", chr(164), " ", end="")
        nome = input("NOME: ").strip()
        print("\n", chr(164), " ", end="")
        descrição = input("DESCRIÇÃO: ").strip()
        print("\n", chr(164), " ", end="")
        categoria = Categoria(codigo, nome, descrição)
        if categoria not in self.categorias:
            self.categorias.append(categoria)
            self.save_categoria()
            print("Categoria Adicionada com sucesso!\n")
            return categoria.nome
        else:
            print("Categoria ou Código já existente\n")

    def create_subcategoria(self):
        """"
        Cria uma categoria através dos dados recolhidos pelo formulário.
        Os dados são: Codigo, nome e descrição e a passagem de um objeto categoria
        """
        print(chr(164)*25, "- CRIAR SUBCATEGORIA -", chr(164)*25)
        if len(self.categorias) == 0:
            print("Não há categorias registradas!\nVocê deve criar pelo menos uma CATEGORIA!\n")
            # self.create_categoria()
            return 1
        print("\n", chr(164), " ", end="")
        codigo = input("CÓDIGO: ").strip()
        print("\n", chr(164), " ", end="")
        nome = input("NOME: ").strip()
        print("\n", chr(164), " ", end="")
        descrição = input("DESCRIÇÃO: ").strip()
        print("\n", chr(164), " ", end="")
        escolhe = input("CATEGORIA (Nome ou Código): ")

        for cat in self.categorias:

            if cat.nome == escolhe or cat.codigo == escolhe:
                print(cat.nome, cat.codigo, escolhe)
                categoria = cat.nome
                subcategoria = Subcategoria(categoria, codigo, nome, descrição)
                break
        else:
            print(cat.nome, cat.codigo, escolhe)
            print("ATENÇÃO! Categoria não Encontrada.\nVocê deve criar uma CATEGORIA!")
            print("\nDeseja Criar uma Categoria? (S/N)")
            opcao = input()
            if opcao.strip() == '1' or opcao.lower() == 'sim' or opcao.lower() == 's':
                newcat = self.create_categoria()
                subcategoria = Subcategoria(newcat, codigo, nome, descrição)

        if subcategoria not in self.subcategorias:
            self.subcategorias.append(subcategoria)
            self.save_subcategorias()
            print("Subcategoria Adicionada com sucesso!")

    def create_produto(self):
        """"
        Cria produto a ser controlado pelo estoque. Um produto deve pertencer a uma subcategoria.
        Produtos são itens que podem ser vendidos.
        Possuem subcategoria, codigo, nome, descricao, estoquemax, estoquemin, valorvenda, valorcompra, foto

        TODELETE: Por enquanto foto recebe uma string qualquer

        """
        # TODO: Implementar a foto no sistemas
        if not len(self.subcategorias):
            print("Produto deve ter CATEGORIA ou uma SUBCATEGORIA!\n")
            self.create_subcategoria()
        else:
            print(chr(164)*25, "- Cadastrar PRODUTO -", chr(164)*25)
            print("\n", chr(164), " ", end="")
            escolhe = input("SUBCATEGORIA (Nome ou Código): ").lower()
            print("\n", chr(164), " ", end="")
            codigo = input("CÓDIGO: ").strip()
            print("\n", chr(164), " ", end="")
            nome = input("NOME: ").strip()
            print("\n", chr(164), " ", end="")
            descricao = input("DESCRIÇÃO: ").strip()
            print("\n", chr(164), " ", end="")
            estoquemax = input("Quantidade Maxima em Estoque: ")
            while not Produtos.valida_estoque(estoquemax):
                print("Valor Inválido!")
                estoquemax = input("Valor deve ser Numérico: ")
            estoquemax = int(estoquemax)
            print("\n", chr(164), " ", end="")
            estoquemin = input("Quantidade Minima em Estoque: ")
            while not Produtos.valida_estoque(estoquemin):
                print("Valor Inválido!")
                estoquemin = input("Valor deve ser Numérico: ")
            estoquemin = int(estoquemin)
            print("\n", chr(164), " ", end="")
            quantidade = input("Quantidade Atual em Estoque: ")
            while not Produtos.valida_estoque(quantidade):
                print("Valor Inválido!")
                quantidade = input("Valor deve ser Numérico: ")
            quantidade = int(quantidade)
            print("\n", chr(164), " ", end="")
            valorvenda = input("Preço Unitário: ")
            while not Produtos.valida_valorvenda(valorvenda):
                print("Valor Inválido!")
                valorvenda = input("Valor deve ser Numérico: ")
            valorvenda = float(valorvenda.replace(",", "."))
            print("\n", chr(164), " ", end="")
            valorcompra = input("Valor de Compra: ")
            while not Produtos.valida_valorvenda(valorcompra):
                print("Valor Inválido!")
                valorcompra = input("Valor deve ser Numérico: ")
            valorcompra = float(valorcompra.replace(",", "."))
            print("\n", chr(164), " ", end="")
            foto = input("Arquivo de foto: ")                  # a ideia é receber um objeto file para arquivos de fotos
            # TODO: Criar codigo para tratar imagens

        subcategoria = 0
        for scat in self.subcategorias:
            if scat.nome.lower() == escolhe or scat.codigo == escolhe:
                subcategoria = scat
                break
        else:                                                                  # saiu do laço e n encontrou subcategoria
            print("Subcategoria não Encontrada!\nDeseja criar uma SUBCATEGORIA?\n1- Sim\n2 - Não")
            choice = input()
            if choice.lower() == 's' or choice == '1' or choice.lower() == 'sim':
                self.create_subcategoria()
            else:
                self.create_produto()

        produto = Produtos(subcategoria, codigo, nome, descricao, estoquemax, estoquemin, quantidade, valorvenda,
                           valorcompra, foto)

        if produto not in self.produtos:
            self.produtos.append(produto)
            self.save_produtos()
            print("Produto Adicionado com Sucesso!")

    # funcionalidade pedida na especificação

    def low_stock_alarm(self):                                                                  # aviso de estoque baixo
        """
             AVISO DE ESTOQUE BAIXO:
                Printa na tela uma lista de produtos que apresentam quantidade em estoque menor que a quantidade mínima
                percorre toda a lista de produtos cadastrados e verifica se a quantidade atual de cada produto é menor
                ou igual a quantidade mínima estabelecida

            :return: produtos com estoque baixo
        """
        if len(self.produtos):
            # print("\n**********Lista de Produtos com estoque abaixo do Minimo: **********")
            for produto in self.produtos:
                if produto.quantidade <= produto.estoquemin:
                    print("\n\nATENÇÃO! %s em quantidade baixa! Abaixo de %d\n\n" % (produto.nome, produto.estoquemin))

    def consulta_estoque(self):                                                     # exibe itens disponiveis no estoque
        """"
        Metodo Consulta_estoque: Exibe na tela os itens que estão registrados
        Retorna se houver:
            >Lista de Categorias Registradas
            >Lista de Subcategorias Registradas
            >Lista de Produtos Registrados
        """

        print(chr(164) * 18, "- Sistema de Vendas ao Consumidor -", chr(164) * 18)
        print(chr(164) * 25, "- CONSULTAR ESTOQUE -", chr(164) * 25)
        print("Escolha:\n1- Consultar Produtos\n2- Consultar Categoria\n3- Consultar Sub-Categoria\n0- SAIR")
        opcao = input()

        while not self.valida_opcao(opcao, "0123"):
            print("Opção Inválida!")
            opcao = input()
        while opcao:
            if opcao == '1':
                if not len(self.produtos):
                    print("Não há Produtos Registrados!\n")
                    break
                else:
                    for produto in self.produtos:
                        if produto == self.produtos[len(self.produtos) - 1]:
                            print(produto)
                        else:
                            print(produto, end=" ")
                    break
            elif opcao == '2':
                if not len(self.categorias):
                    print("Não há Categorias Registradas!\n")
                    break
                else:
                    print("CODIGO\t\tNOME:\t\tDESCRIÇÃO")
                    for categoria in self.categorias:
                        print(categoria)
                    break
            elif opcao == '3':
                if not len(self.subcategorias):
                    print("\nNão há Subcategorias Registradas!\n")
                    break
                else:
                    print("CODIGO\t\tNOME:\t\tCATEGORIA\t\tDESCRIÇÃO")
                    for subcategoria in self.subcategorias:
                        print(subcategoria)
                    break

    def altera_item(self):      # altera um item disponivel no estoque
        """
        Altera item - Altera parametros do objeto escolhido
        qualquer parametro pode ser alterado

        Se você não desejar alterar um parametro pode simplemente deixa-lo em branco e digitar <ENTER>

        :return: objeto escolhido alterado.
        """
        while True:
            print(chr(164)*15, "Escolha o Item que deseja ALTERAR", chr(164)*15)
            print(chr(164), "1- Alterar uma categoria\n", chr(164), "2- Alterar uma Subcategoria\n", chr(164),
                  "3- Alterar um produto\n", chr(164), "0 - SAIR")
            opcao = input()

            while not self.valida_opcao(opcao, "0123"):
                print("Opção Inválida!")
                opcao = input()

            if opcao == '1':
                if not len(self.categorias):
                    print("Não há Categorias Registradas!\n")
                else:
                    print("Escolha ma Categoria: ")
                    [print(categoria.codigo, categoria.nome, end="**") for categoria in self.categorias]
                    opcao = input("\nDigite Código Escolhido: ")
                    for categoria in self.categorias:
                        if categoria.codigo == opcao:
                            print("Deixe em branco (PRESS ENTER) para não alterar o campo!")
                            nome = input("\nDigite Nome: ")
                            if nome == "":
                                pass
                            else:
                                categoria.nome = nome

                            codigo = input("Digite Código: ")
                            if codigo == "":
                                pass
                            else:
                                categoria.codigo = codigo
                            descricao = input("Digite Descrição: ")
                            if descricao == "":
                                pass
                            else:
                                categoria.descricao = descricao
                        else:
                            print("Codigo não encontrado!\n")

                    self.save_categoria()

            elif opcao == '2':
                if not len(self.subcategorias):
                    print("Não há Subategorias Registradas!\n")
                else:
                    print("Escolha uma Subtegoria: ")
                    [print(subcategoria.codigo, subcategoria.nome, end="**") for subcategoria in self.subcategorias]
                    opcao = input("\nDigite Código Escolhido: ")
                    for subcategoria in self.subcategorias:
                        if subcategoria.codigo == opcao:
                            print("Deixe em branco (PRESS ENTER) para não alterar o campo!")
                            nome = input("\nDigite Nome: ")
                            if nome == "":
                                pass
                            else:
                                subcategoria.nome = nome

                            codigo = input("Digite Código: ")
                            if codigo == "":
                                pass
                            else:
                                subcategoria.codigo = codigo
                            descricao = input("Digite Descrição: ")
                            if descricao == "":
                                pass
                            else:
                                subcategoria.descricao = descricao
                        else:
                            print("Codigo não encontrado!\n")
                    self.save_subcategorias()

            elif opcao == '3':
                if not len(self.produtos):
                    print("Não há Produtos Registrados!\n")
                else:
                    print("Escolha um Produto: ")
                    [print(produto.codigo, produto.nome, end="**") for produto in self.produtos]
                    opcao = input("Digite Código Escolhido: ")
                    for produto in self.produtos:
                        if produto.codigo == opcao:
                            print("Deixe em branco (PRESS ENTER) para não alterar o campo!")
                            nome = input("\nDigite Nome: ")
                            if nome == "":
                                pass        # Se não for mexido nesse campo nada é feito
                            else:
                                produto.nome = nome

                            codigo = input("\nDigite Código: ")
                            if codigo == "":
                                pass  # Se não for mexido nesse campo nada é feito
                            else:
                                produto.codigo = codigo

                            descricao = input("\nDigite Descrição: ")
                            if descricao == "":
                                pass  # Se não for mexido nesse campo nada é feito
                            else:
                                produto.descricao = descricao
                        else:
                            print("Codigo não encontrado!\n")
                    print("\nProduto Alterado com Sucesso!\n")
                    self.save_produtos()

            elif opcao == '0':
                break

    def remove_item(self):    # remove um item disponivel no estoque - n remover se o item ainda tem produtos no estoque
        """
        Escolhe um tipo de item a ser removido do sistema de estoque
        Apos escolhido o objeto é remadado o metodo del daquele objeto e então é destruido e removido da lista
        de objetos

        Se o item escolhido já tiver sido negociado não pode ser removido

        :return: Sucess - "Item Removido com Sucesso!" or Fail - "Item não pode ser removido!"
        """

        print("Removendo item do estoque")

        while 1:
            print("Digite o tipo de ITEM que deseja remover:\n1- Categoria\n2- Subcategoria\n3- Produto\n0 - SAIR")

            opcao = input()

            while not funcionalidades.valida_opcao(opcao, "0123"):
                print("Opção Inválida!")
                opcao = input()

            if opcao == '1':
                if not len(self.categorias):
                    print("Não há Categorias Registradas!\n")
                else:
                    print("Escolha uma Categoria: ")
                    [print(categoria.codigo, categoria.nome) for categoria in self.categorias]
                    opcao = input("\nDigite Código Escolhido: ")
                    for categoria in self.categorias:
                        if categoria.codigo == opcao:
                            index = self.categorias.index(categoria)
                            del self.categorias[index]
                            print("\nCategoria Removida com Sucesso!")
                            self.save_categoria()
                            break
                        else:
                            print("Codigo não encontrado!\n")

            elif opcao == '2':
                if not len(self.subcategorias):
                    print("Não há Subategorias Registradas!\n")
                else:
                    print("Escolha uma Subtegoria: ")
                    [print(subcategoria.codigo, subcategoria.nome, end="**") for subcategoria in self.subcategorias]
                    opcao = input("\nDigite Código Escolhido: ")
                    for subcategoria in self.subcategorias:
                        if subcategoria.codigo == opcao:
                            index = self.subcategorias.index(subcategoria)
                            del self.subcategorias[index]
                            print("\nSubcategoria Removida com Sucesso!")
                            self.save_subcategorias()
                            break
                        else:
                            print("Codigo não encontrado!\n")

            elif opcao == '3':
                if not len(self.produtos):
                    print("Não há Produtos Registrados!\n")
                else:
                    print("Escolha um Produto: ")
                    [print(produto.codigo, produto.nome) for produto in self.produtos]
                    opcao = input("\nDigite Código Escolhido: ")
                    for produto in self.produtos:
                        if produto.codigo == opcao:
                            if not produto.ativo:
                                index = self.produtos.index(produto)
                                del self.produtos[index]
                                print("\nProduto Removido com Sucesso!!\n")
                                self.save_produtos()
                                break
                            else:
                                print("ATENÇÃO! Produto já negociado não pode ser removido", file=funcionalidades.warning)
                        else:
                            print("Codigo não encontrado!\n")
            elif opcao == '0':
                break

    def adiciona_item(self):     # adiciona novo item ao estoque
        print("Adicionando item ao estoque")
        while 1:
            print(chr(164)*25, "- Menu Adicionar -", chr(164)*25)
            print("\n1 - Adicionar Categoria\n2 - Adicionar Subcategoria\n3 - Adicionar Produtos\n0 - Sair")
            opcao = input()
            while not self.valida_opcao(opcao, "0123"):
                print("Opção Inválida!")
                opcao = input()
            if opcao == '1':
                self.create_categoria()
            elif opcao == '2':
                self.create_subcategoria()
            elif opcao == '3':
                self.create_produto()
            elif opcao == '0':
                break

    def menu_estoque(self):
        os.system('cls')
        while True:
            print(chr(164) * 79)
            print("Sistema de Vendas ao Consumidor".center(80))
            print(chr(164) * 79)
            print(chr(164) * 29, "- MENU DE ESTOQUE -", chr(164) * 29)
            print("\n1 - Consultar Estoque\n2 - Adicionar\n3 - Remover\n4 - Alterar\n0 - SAIR")
            opcao = input()

            while not self.valida_opcao(opcao, "01234"):
                print("Opção Inválida!")
                opcao = input()

            if opcao == '1':
                self.consulta_estoque()
            elif opcao == '2':
                self.adiciona_item()
            elif opcao == '3':
                self.remove_item()
            elif opcao == '4':
                self.altera_item()
            elif opcao == '0':
                break

    def valida_opcao(self, opcao, options):
        if opcao.isdigit() and opcao in options:
            return True
        else:
            return False
