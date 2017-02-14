import funcionalidades
import pickle


class Loja(object):
    def __init__(self, cadastro, razao, endereco, logo, bairro, uf, dono, cep, email, url, cidade, fantasia,
                   telefone):
        self.__cadastro = cadastro
        self.__razao = razao
        self.__endereco = endereco
        self.__logo = logo
        self.__bairro = bairro
        self.__uf = uf
        self.__dono = dono
        self.__cep = cep
        self.__email = email
        self.__url = url
        self.__cidade = cidade
        self.__fantasia = fantasia
        self.__telefone = telefone
        self.loja = None
        self.load()

    def save(self):
        pass

    def load(self):
        try:
            with open('loja.vdc', 'rb') as lojaconfig:
                self.loja = pickle.load(lojaconfig)
        except FileNotFoundError:
            print("Loja precisa ser configurada")

            # metodos getters e setters

        @property
        def razao ( self ):
            return self.__razao

        @razao.setter
        def razao ( self, valor ):
            while not funcionalidades.valida_nome(valor):
                print("Nome ou Razão Social Inválido!")
                print(chr(847), end='')
                valor = input("Razão Social: ")
            else:
                self.__razao = valor

        @property
        def endereco (self ):
            return self.__endereco

        @endereco.setter
        def endereco ( self, valor ):
            while not self.valida_endereco(valor):
                print("Endereço Inválido")
                valor = input("ENDEREÇO: ")
            else:
                self.__endereco = valor

        @property
        def numero ( self ):
            return self.__numero

        @numero.setter
        def numero ( self, valor ):
            while not self.valida_numero(valor):
                print("Número Inválido")
                valor = input("NÚMERO: ")
            else:
                self.__numero = valor

        @property
        def complemento ( self ):
            return self.__complemento

        @complemento.setter
        def complemento ( self, valor ):
            self.__complemento = valor

        @property
        def bairro ( self ):
            return self.__bairro

        @bairro.setter
        def bairro ( self, valor ):
            while not self.valida_bairro(valor):
                print("Bairro Inválido")
                valor = input("BAIRRO: ")
            else:
                self.__bairro = valor

        @property
        def cidade ( self ):
            return self.__cidade

        @cidade.setter
        def cidade ( self, valor ):
            while not self.valida_cidade(valor):
                print("Cidade Inválida")
                valor = input("CIDADE: ")
            else:
                self.__cidade = valor

        @property
        def estado ( self ):
            return self.__estado

        @estado.setter
        def estado ( self, valor ):
            while not self.valida_estado(valor):
                print("Estado Inválido")
                valor = input("UF: ")
            else:
                self.__estado = valor

        @property
        def telefone ( self ):
            return self.__telefone

        @telefone.setter
        def telefone ( self, valor ):
            while not self.valida_telefone(valor):
                print("Telefone Inválido")
                valor = input("TELEFONE: ")
            else:
                self.__telefone = valor

        @property
        def celular ( self ):
            return self.__celular

        @celular.setter
        def celular ( self, valor ):
            while not self.valida_celular(valor):
                print("Celular Inválido")
                valor = input("CELULAR: ")
            else:
                self.__celular = valor

        @property
        def email ( self ):
            return self.__email

        @email.setter
        def email ( self, valor ):
            while not self.valida_email(valor):
                print("Email Inválido")
                valor = input("EMAIL: ")
            else:
                self.__email = valor

        @property
        def rg ( self ):
            return self.__rg

        @rg.setter
        def rg ( self, valor ):
            while not self.valida_rg(valor):
                print("RG Inválido")
                valor = input("RG: ")
            else:
                self.__rg = valor

        @property
        def cadastro ( self ):
            return self.__cadastro

        @cadastro.setter
        def cadastro ( self, valor ):
            while not self.valida_cadastro(valor):
                print("CPF\CNPJ Inválido")
                valor = input("Cadastro(CPF ou CNPJ): ")
            else:
                self.__cadastro = valor

        @property
        def cep ( self ):
            return self.__cep

        @cep.setter
        def cep ( self, valor ):
            while not self.valida_cep(valor):
                print("CEP Inválido")
                valor = input("CEP: ")
            else:
                self.__cep = valor

    def altera(self):
        pass

    @staticmethod
    def configurar_loja():
        print("OLÁ! BEM VINDO AO SVC!\n\nVamos ajudá-lo a configurar seu sistema.\nComece informando os dados da loja!")
        print("\nCONFIGURANDO LOJA...")

        print(chr(847), end='')
        razao = input("Razão Social: ")
        while not funcionalidades.valida_nome(razao, "loja"):
            print(chr(847), end='')
            razao = input("Razão Social: ")

        print(chr(847), end='')
        cadastro = input("CNPJ: ")
        while not funcionalidades.valida_cadastro(cadastro):
            print(chr(847), end='')
            cadastro = input("CNPJ: ")


if __name__ != "__main__":
    try:
        with open('loja.vdc', 'rb') as lojaconfig:
            Loja = pickle.load(lojaconfig)
    except FileNotFoundError:
        Loja.configurar_loja()
