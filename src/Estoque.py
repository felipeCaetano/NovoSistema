from produtos import *


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
        print("***** CRIAR SUBCATEGORIA: ******")
        if len(self.categorias) == 0:
            print("Não há categorias registradas!\nVocê deve criar pelo menos uma CATEGORIA!\n")
            # self.create_categoria()
            return 1
        print("- Criar SUBCATEGORIA -")
        codigo = input("CÓDIGO: ").strip()
        nome = input("NOME: ").strip()
        descrição = input("DESCRIÇÃO: ").strip()
        escolhe = input("CATEGORIA (Nome ou Código): ")
        # categoria = 0

        for cat in self.categorias:
            if cat.nome == escolhe or cat.codigo == escolhe:
                categoria = cat
                subcategoria = Subcategoria(categoria, codigo, nome, descrição)
                break
            else:
                print("Categoria não Encontrada!\nVocê deve criar uma CATEGORIA!")
                print("Deseja Criar um Subcategoria? (1- Sim /2- Não)")
                opcao = input()
                if opcao.strip() == '1' or opcao.lower() == 'sim' or opcao.lower() == 's':
                    newcat = self.create_categoria()
                    subcategoria = Subcategoria(newcat, codigo, nome, descrição)
                    break
                else:
                    break

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

            quantidade = input("Quantidade Atual em Estoque: ")
            while not Produtos.valida_estoque(quantidade):
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

            foto = input("Arquivo de foto: ")                  # a ideia é receber um objeto file para arquivos de fotos

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

        produto = Produtos(subcategoria, codigo, nome, descricao, estoquemax, estoquemin, quantidade, valorvenda, valorcompra, foto)

        if produto not in self.produtos:
            self.produtos.append(produto)
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
            print("\n**********Lista de Produtos com estoque abaixo do Minimo: **********")
            for produto in self.produtos:
                if produto.quantida <= produto.estoquemin:
                    print("%s em quantidade baixa! Abaixo de %d" % (produto.nome, produto.estoquemin))
            else:
                print("Os produtos não listados não precisam de reposições no momento.")

    def consulta_estoque(self):                                                     # exibe itens disponiveis no estoque
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
            print("CODIGO\t\tNOME:\t\tDESCRIÇÃO")
            for categoria in self.categorias:
                print(categoria)

        if not len(self.subcategorias):
            print("\nNão há Subcategorias Registradas!\n")
        else:
            print("CODIGO\t\tNOME:\t\tCATEGORIA\t\tDESCRIÇÃO")
            for subcategoria in self.subcategorias:
                print(subcategoria)

        if not len(self.produtos):
            print("Não há Produtos Registrados!\n")
        else:
            for produto in self.produtos:
                if produto == self.produtos[len(self.produtos)-1]:
                    print(produto)
                else:
                    print(produto, end=" ")

    def altera_item(self):      # altera um item disponivel no estoque
        """
        Altera item - Altera parametros do objeto escolhido
        qualquer parametro pode ser alterado

        Se você não desejar alterar um parametro pode simplemente deixa-lo em branco e digitar <ENTER>

        :return: objeto escolhido alterado.
        """
        while True:
            print("Escolha o Item que deseja ALTERAR")
            print("1- Alterar uma categoria\n2- Alterar uma Subcategoria\n3- Alterar um produto\n0 - SAIR")
            opcao = input()

            while not self.valida_opcao(opcao):
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

            while not self.valida_opcao(opcao):
                print("Opção Inválida!")
                opcao = input()

            if opcao == '1':
                if not len(self.categorias):
                    print("Não há Categorias Registradas!\n")
                else:
                    print("Escolha uma Categoria: ")
                    [print(categoria.codigo, categoria.nome, end="**") for categoria in self.categorias]
                    opcao = input("\nDigite Código Escolhido: ")
                    for categoria in self.categorias:
                        if categoria.codigo == opcao:
                            index = self.categorias.index(categoria)
                            del self.categorias[index]
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
                            break
                        else:
                            print("Codigo não encontrado!\n")

            elif opcao == '3':
                if not len(self.produtos):
                    print("Não há Produtos Registrados!\n")
                else:
                    print("Escolha um Produto: ")
                    [print(produto.codigo, produto.nome, end="**") for produto in self.produtos]
                    opcao = input("\nDigite Código Escolhido: ")
                    for produto in self.produtos:
                        if produto.codigo == opcao:
                            index = self.produtos.index(produto)
                            del self.produtos[index]
                            break
                        else:
                            print("Codigo não encontrado!\n")

            elif opcao == '0':
                break

    def adiciona_item(self):     # adiciona novo item ao estoque
        print("Adicionando item ao estoque")
        while 1:
            print("************* Menu Adicionar: ******************")
            print("Digite Ação!\n1 - Adicionar Categoria\n2 - Adicionar Subcategoria\n3 - Adicionar Produtos\n0 - Sair")
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
            elif opcao == '0':
                break

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
        if opcao.isdigit() and opcao in "01234":
            return True
        else:
            return False

estoque = Estoque()
