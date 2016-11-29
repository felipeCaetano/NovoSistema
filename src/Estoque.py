from src.produtos import *


class Estoque(object):
    def __init__(self):
        self.categorias = []
        self.subcategorias = []
        self.produtos = []
        self.menu_estoque()

    def save_categoria(self, categoria):
        pass

    def save_subcategorias(self, subcategoria):
        pass

    def save_produtos(self, produto):
        pass

    def create_categoria(self):
        """"
        Cria uma categoria através dos dados recolhidos pelo formulário.
        Os dados são: Codigo, nome e descrição
        """
        print("- Criar CATEGORIA -")
        codigo = input("CÓDIGO: ").strip()
        nome = input("NOME: ").strip()
        descrição = input("DESCRIÇÃO: ").strip()
        categoria = Categoria(codigo, nome, descrição)
        if categoria not in self.categorias:
            self.categorias.append(categoria)
            print("Categoria Adicionada com sucesso!")

    def create_subcategoria(self):
        """"
        Cria uma categoria através dos dados recolhidos pelo formulário.
        Os dados são: Codigo, nome e descrição e a passagem de um objeto categoria
        """
        if len(self.categorias) == 0:
            print("Você deve criar pelo menos uma CATEGORIA!\n")
            self.create_categoria()
        print("- Criar SUBCATEGORIA -")
        codigo = input("CÓDIGO: ").strip()
        nome = input("NOME: ").strip()
        descrição = input("DESCRIÇÃO: ").strip()
        escolhe = input("CATEGORIA (Nome ou Código): ")
        categoria = 0

        for cat in self.categorias:
            if cat.nome == escolhe or cat.codigo == escolhe:
                categoria = cat
                break
            else:
                print("Categoria não Encontrada!\nVocê deve criar uma CATEGORIA!")
                self.create_categoria()

        subcategoria = Subcategoria(categoria, codigo, nome, descrição)

        if subcategoria not in self.subcategorias:
            self.subcategorias.append(subcategoria)
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
            print("- Cadastrar PRODUTO -")
            escolhe = input("SUBCATEGORIA (Nome ou Código): ").lower()
            codigo = input("CÓDIGO: ").strip()
            nome = input("NOME: ").strip()
            descricao = input("DESCRIÇÃO: ").strip()

            estoquemax = input("Quantidade Maxima em Estoque: ")
            while not Produtos.valida_estoque(estoquemax):
                print("Valor Inválido!")
                estoquemax = input("Valor deve ser Numérico: ")

            estoquemin = input("Quantidade Minima em Estoque: ")
            while not Produtos.valida_estoque(estoquemin):
                print("Valor Inválido!")
                estoquemin = input("Valor deve ser Numérico: ")

            valorvenda = input("Preço Unitário: ")
            while not Produtos.valida_valorvenda(valorvenda):
                print("Valor Inválido!")
                estoquemax = input("Valor deve ser Numérico: ")

            valorcompra = input("Valor de Compra: ")
            while not Produtos.valida_valorvenda(valorcompra):
                print("Valor Inválido!")
                estoquemax = input("Valor deve ser Numérico: ")

            foto = input("Arquivo de foto: ")

            subcategoria = 0

        for scat in self.subcategorias:
            if scat.nome.lower() == escolhe or scat.codigo == escolhe:
                subcategoria = scat
                break
            else:
                print("Subcategoria não Encontrada!\nDeseja criar uma SUBCATEGORIA?\n1- Sim\n2 - Não")
                choice = input()
                if choice.lower() == 's' or choice == '1':
                    self.create_subcategoria()
                else:
                    self.create_produto()

            produto = Produtos( subcategoria, codigo, nome, descricao, estoquemax, estoquemin, valorvenda, valorcompra, foto)

        if produto not in self.produtos:
            self.produtos.append(produto)
            print("Produto Adicionado com sucesso!")

    # funcionalidade pedida na especificação

    def low_stock_alarm(self):  # aviso de estoque baixo
        pass

    def consulta_estoque(self):    # exibe itens disponiveis no estoque
        """"
        Metodo Consulta_estoque: Exibe na tela os itens que estão registrados
        Retorna se houver:
            >Lista de Categorias Registradas
            >Lista de Subcategorias Registradas
            >Lista de Produtos Registrados
        """
        print("Exibindo Estoque\n")
        if not len(self.categorias):
            print("Não há Categorias Registradas!\n")
        else:
            for categoria in self.categorias:
                if categoria == self.categorias[len(self.categorias)-1]:
                    print(categoria)
                else:
                    print(categoria, end=" ")

        if not len(self.subcategorias):
            print("Não há Subcategorias Registradas!\n")
        else:
            for subcategoria in self.subcategorias:
                if subcategoria == self.subcategorias[len(self.subcategorias)-1]:
                    print(subcategoria)
                else:
                    print(subcategoria, end=" ")

        if not len(self.produtos):
            print("Não há Produtos Registrados!\n")
        else:
            for produto in self.produtos:
                if produto == self.produtos[len(self.subcategorias)-1]:
                    print(produto)
                else:
                    print(produto, end=" ")

        self.menu_estoque()

    def altera_item(self):      # altera um item disponivel no estoque
        print("alterando item do estoque")
        self.menu_estoque()

    def remove_item(self):    # remove um item disponivel no estoque - n remover se o item ainda tem produtos no estoque
        print("Removendo item do estoque")
        self.menu_estoque()

    def adiciona_item(self):     # adiciona novo item ao estoque
        print("Adicionando item ao estoque")
        while 1:
            print("************* Menu Adicionar: ******************")
            print("Digite Ação!\n1 - Adicionar Categoria\n2 - Adicionar Subcategoria\n3 - Adicionar Produtos\n4 - Sair")
            opcao = input()
            while not self.valida_opcao(opcao):
                print("Opção Inválida!")
                opcao = input()
            if opcao == '1':
                self.create_categoria()
            elif opcao == '2':
                self.create_subcategoria()
            elif opcao == '3':
                self.create_produto()
            elif opcao == '4':
                break
        self.menu_estoque()

    def menu_estoque(self):
        while True:
            print("Sistema de Vendas ao Consumidor")
            print("****** MENU DE ESTOQUE *****")
            print("Digite Ação!\n1 - Consultar Estoque\n2 - Adicionar\n3 - Remover\n4 - Alterar\n0 - SAIR")
            opcao = input()

            while not self.valida_opcao(opcao):
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

    def valida_opcao(self, opcao):
        if opcao.isdigit():
            return True
        else:
            return False

estoque = Estoque()
