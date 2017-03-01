<<<<<<< HEAD
import funcionalidades
import pickle


class Loja(object):
    def __init__(self, cadastro, razao, fantasia, endereco, cidade, bairro,  cep, uf, email, url, logo,
                   telefone):
        self.__fantasia = fantasia
        self.__cadastro = cadastro
        self.__razao = razao
        self.__endereco = endereco
        self.__logo = logo
        self.__bairro = bairro
        self.__uf = uf
        self.__cep = cep
        self.__email = email
        self.__url = url
        self.__cidade = cidade
        #self._fantasia = fantasia
        self.__telefone = telefone
        self.save()

    def save(self):
        with open('loja.vdc', 'wb') as arquivo_config:
            pickle.dump(self, arquivo_config)

    def load(self):
        try:
            with open('loja.vdc', 'rb') as lojaconfig:
                self.loja = pickle.load(lojaconfig)
        except FileNotFoundError:
            print("ATENÇÃO! Loja precisa ser configurada")

            # metodos getters e setters

    @property
    def fantasia(self):
        return self.__fantasia

    @fantasia.setter
    def fantasia(self, valor):
        while not funcionalidades.valida_nome(valor):
            print("Nome Fantasia Inválido!")
            print(chr(164), end='')
            valor = input("Nome Fantasia: ")
        self.__fantasia = valor

        # @property
        # def endereco ( self ):
        #     return self.__endereco
        #
        # @endereco.setter
        # def endereco ( self, valor ):
        #     while not self.valida_endereco(valor):
        #         print("Endereço Inválido")
        #         valor = input("ENDEREÇO: ")
        #     else:
        #         self.__endereco = valor
        #
        # @property
        # def numero ( self ):
        #     return self.__numero
        #
        # @numero.setter
        # def numero ( self, valor ):
        #     while not self.valida_numero(valor):
        #         print("Número Inválido")
        #         valor = input("NÚMERO: ")
        #     else:
        #         self.__numero = valor
        #
        # @property
        # def complemento ( self ):
        #     return self.__complemento
        #
        # @complemento.setter
        # def complemento ( self, valor ):
        #     self.__complemento = valor
        #
        # @property
        # def bairro ( self ):
        #     return self.__bairro
        #
        # @bairro.setter
        # def bairro ( self, valor ):
        #     while not self.valida_bairro(valor):
        #         print("Bairro Inválido")
        #         valor = input("BAIRRO: ")
        #     else:
        #         self.__bairro = valor
        #
        # @property
        # def cidade ( self ):
        #     return self.__cidade
        #
        # @cidade.setter
        # def cidade ( self, valor ):
        #     while not self.valida_cidade(valor):
        #         print("Cidade Inválida")
        #         valor = input("CIDADE: ")
        #     else:
        #         self.__cidade = valor
        #
        # @property
        # def estado ( self ):
        #     return self.__estado
        #
        # @estado.setter
        # def estado ( self, valor ):
        #     while not self.valida_estado(valor):
        #         print("Estado Inválido")
        #         valor = input("UF: ")
        #     else:
        #         self.__estado = valor
        #
        # @property
        # def telefone ( self ):
        #     return self.__telefone
        #
        # @telefone.setter
        # def telefone ( self, valor ):
        #     while not self.valida_telefone(valor):
        #         print("Telefone Inválido")
        #         valor = input("TELEFONE: ")
        #     else:
        #         self.__telefone = valor
        #
        # @property
        # def celular ( self ):
        #     return self.__celular
        #
        # @celular.setter
        # def celular ( self, valor ):
        #     while not self.valida_celular(valor):
        #         print("Celular Inválido")
        #         valor = input("CELULAR: ")
        #     else:
        #         self.__celular = valor
        #
        # @property
        # def email ( self ):
        #     return self.__email
        #
        # @email.setter
        # def email ( self, valor ):
        #     while not self.valida_email(valor):
        #         print("Email Inválido")
        #         valor = input("EMAIL: ")
        #     else:
        #         self.__email = valor
        #
        # @property
        # def rg ( self ):
        #     return self.__rg
        #
        # @rg.setter
        # def rg ( self, valor ):
        #     while not self.valida_rg(valor):
        #         print("RG Inválido")
        #         valor = input("RG: ")
        #     else:
        #         self.__rg = valor

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

        # @property
        # def cep ( self ):
        #     return self.__cep
        #
        # @cep.setter
        # def cep ( self, valor ):
        #     while not self.valida_cep(valor):
        #         print("CEP Inválido")
        #         valor = input("CEP: ")
        #     else:
        #         self.__cep = valor

    def altera(self):
        pass

    @staticmethod
    def configurar_loja():
        print("OLÁ! BEM VINDO AO SVC!\n\nVamos ajudá-lo a configurar seu sistema.\nComece informando os dados da loja!")
        print("\nCONFIGURANDO LOJA...")

        print(chr(164), end='')
        razao = input("Razão Social: ")
        while not funcionalidades.valida_nome(razao, "loja"):
            print(chr(164), end='')
            razao = input("Razão Social: ")

        print(chr(164), end='')
        fantasia = input("NOME FANTASIA: ")
        while not funcionalidades.valida_nome(fantasia, "loja"):
            print(chr(164), end='')
            fantasia = input("NOME FANTASIA: ")

        print(chr(164), end='')
        cadastro = input("CNPJ: ")
        while not funcionalidades.valida_cadastro(cadastro):
            print(chr(164), end='')
            cadastro = input("CNPJ: ")

        print(chr(164), end='')
        endereco = input("ENDEREÇO: ")
        while not funcionalidades.valida_endereco(endereco):
            print(chr(164), end='')
            endereco = input("ENDEREÇO: ")

        print(chr(164), end='')
        bairro = input("BAIRRO: ")
        while not funcionalidades.valida_bairro(bairro):
            print(chr(164), end='')
            bairro = input("BAIRRO: ")

        print(chr(164), end='')
        cidade = input("CIDADE: ")
        while not funcionalidades.valida_cidade(cidade):
            print(chr(164), end='')
            cidade = input("CIDADE: ")

        print(chr(164), end='')
        uf = input("UF: ")
        while not funcionalidades.valida_estado(uf):
            print(chr(164), end='')
            uf = input("UF: ")

        print(chr(164), end='')
        cep = input("CEP: ")
        while not funcionalidades.valida_cep(cep):
            print(chr(164), end='')
            cep = input("CEP: ")

        print(chr(164), end='')
        email = input("EMAIL: ")
        while not funcionalidades.valida_email(email):
            print(chr(164), end='')
            email = input("EMAIL: ")

        print(chr(164), end='')
        url = input("SITE: ")
        while not funcionalidades.valida_url(url):
            print(chr(164), end='')
            url = input("SITE: ")

        print(chr(164), end='')
        telefone = input("TELEFONE: ")
        while not funcionalidades.valida_telefone(telefone):
            print(chr(164), end='')
            telefone = input("TELEFONE: ")

        print(chr(164), end='')
        logo = input("LOGOTIPO: ")
        # while not funcionalidades.valida_cadastro(cadastro):
          #  print(chr(164), end='')
          #  cadastro = input("CNPJ: ")

        return (cadastro, razao, fantasia, endereco, cidade, bairro, cep, uf, email, url, logo, telefone)

if __name__ != "__main__":
    try:
        with open('loja.vdc', 'rb') as lojaconfig:
            Loja = pickle.load(lojaconfig)
    except FileNotFoundError:
        cadastro, razao, fantasia, endereco, cidade, bairro, cep, uf, email, url, logo, telefone = Loja.configurar_loja()
        loja = Loja(cadastro, razao, fantasia, endereco, cidade, bairro, cep, uf, email, url, logo, telefone)
        print("\nLoja Cadastrada com Sucesso!\n")

=======
import funcionalidades
import pickle


class Loja(object):
    def __init__(self, cadastro, razao, fantasia, endereco, cidade, bairro,  cep, uf, email, url, logo,
                   telefone):
        self.__fatansia = fantasia
        self.__cadastro = cadastro
        self.__razao = razao
        self.__endereco = endereco
        self.__logo = logo
        self.__bairro = bairro
        self.__uf = uf
        self.__cep = cep
        self.__email = email
        self.__url = url
        self.__cidade = cidade
        #self._fantasia = fantasia
        self.__telefone = telefone
        self.save()

    def save(self):
        with open('loja.vdc', 'wb') as arquivo_config:
            pickle.dump(self, arquivo_config)

    def load(self):
        try:
            with open('loja.vdc', 'rb') as lojaconfig:
                self.loja = pickle.load(lojaconfig)
        except FileNotFoundError:
            print("ATENÇÃO! Loja precisa ser configurada")

            # metodos getters e setters

    @property
    def fantasia(self):
        return self.__fantasia

    @fantasia.setter
    def fantasia(self, valor):
        while not funcionalidades.valida_nome(valor):
            print("Nome Fantasia Inválido!")
            print(chr(847), end='')
            valor = input("Nome Fantasia: ")
        self.__fantasia = valor

        # @property
        # def endereco ( self ):
        #     return self.__endereco
        #
        # @endereco.setter
        # def endereco ( self, valor ):
        #     while not self.valida_endereco(valor):
        #         print("Endereço Inválido")
        #         valor = input("ENDEREÇO: ")
        #     else:
        #         self.__endereco = valor
        #
        # @property
        # def numero ( self ):
        #     return self.__numero
        #
        # @numero.setter
        # def numero ( self, valor ):
        #     while not self.valida_numero(valor):
        #         print("Número Inválido")
        #         valor = input("NÚMERO: ")
        #     else:
        #         self.__numero = valor
        #
        # @property
        # def complemento ( self ):
        #     return self.__complemento
        #
        # @complemento.setter
        # def complemento ( self, valor ):
        #     self.__complemento = valor
        #
        # @property
        # def bairro ( self ):
        #     return self.__bairro
        #
        # @bairro.setter
        # def bairro ( self, valor ):
        #     while not self.valida_bairro(valor):
        #         print("Bairro Inválido")
        #         valor = input("BAIRRO: ")
        #     else:
        #         self.__bairro = valor
        #
        # @property
        # def cidade ( self ):
        #     return self.__cidade
        #
        # @cidade.setter
        # def cidade ( self, valor ):
        #     while not self.valida_cidade(valor):
        #         print("Cidade Inválida")
        #         valor = input("CIDADE: ")
        #     else:
        #         self.__cidade = valor
        #
        # @property
        # def estado ( self ):
        #     return self.__estado
        #
        # @estado.setter
        # def estado ( self, valor ):
        #     while not self.valida_estado(valor):
        #         print("Estado Inválido")
        #         valor = input("UF: ")
        #     else:
        #         self.__estado = valor
        #
        # @property
        # def telefone ( self ):
        #     return self.__telefone
        #
        # @telefone.setter
        # def telefone ( self, valor ):
        #     while not self.valida_telefone(valor):
        #         print("Telefone Inválido")
        #         valor = input("TELEFONE: ")
        #     else:
        #         self.__telefone = valor
        #
        # @property
        # def celular ( self ):
        #     return self.__celular
        #
        # @celular.setter
        # def celular ( self, valor ):
        #     while not self.valida_celular(valor):
        #         print("Celular Inválido")
        #         valor = input("CELULAR: ")
        #     else:
        #         self.__celular = valor
        #
        # @property
        # def email ( self ):
        #     return self.__email
        #
        # @email.setter
        # def email ( self, valor ):
        #     while not self.valida_email(valor):
        #         print("Email Inválido")
        #         valor = input("EMAIL: ")
        #     else:
        #         self.__email = valor
        #
        # @property
        # def rg ( self ):
        #     return self.__rg
        #
        # @rg.setter
        # def rg ( self, valor ):
        #     while not self.valida_rg(valor):
        #         print("RG Inválido")
        #         valor = input("RG: ")
        #     else:
        #         self.__rg = valor

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

        # @property
        # def cep ( self ):
        #     return self.__cep
        #
        # @cep.setter
        # def cep ( self, valor ):
        #     while not self.valida_cep(valor):
        #         print("CEP Inválido")
        #         valor = input("CEP: ")
        #     else:
        #         self.__cep = valor

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
        fantasia = input("NOME FANTASIA: ")
        while not funcionalidades.valida_nome(fantasia, "loja"):
            print(chr(847), end='')
            fantasia = input("NOME FANTASIA: ")

        print(chr(847), end='')
        cadastro = input("CNPJ: ")
        while not funcionalidades.valida_cadastro(cadastro):
            print(chr(847), end='')
            cadastro = input("CNPJ: ")

        print(chr(847), end='')
        endereco = input("ENDEREÇO: ")
        while not funcionalidades.valida_endereco(endereco):
            print(chr(847), end='')
            endereco = input("ENDEREÇO: ")

        print(chr(847), end='')
        bairro = input("BAIRRO: ")
        while not funcionalidades.valida_bairro(bairro):
            print(chr(847), end='')
            bairro = input("BAIRRO: ")

        print(chr(847), end='')
        cidade = input("CIDADE: ")
        while not funcionalidades.valida_cidade(cidade):
            print(chr(847), end='')
            cidade = input("CIDADE: ")

        print(chr(847), end='')
        uf = input("UF: ")
        while not funcionalidades.valida_estado(uf):
            print(chr(847), end='')
            UF = input("UF: ")

        print(chr(847), end='')
        cep = input("CEP: ")
        while not funcionalidades.valida_cep(cep):
            print(chr(847), end='')
            cep = input("CEP: ")

        print(chr(847), end='')
        email = input("EMAIL: ")
        while not funcionalidades.valida_email(email):
            print(chr(847), end='')
            email = input("EMAIL: ")

        print(chr(847), end='')
        url = input("SITE: ")
        while not funcionalidades.valida_url(url):
            print(chr(847), end='')
            url = input("SITE: ")

        print(chr(847), end='')
        telefone = input("TELEFONE: ")
        while not funcionalidades.valida_telefone(telefone):
            print(chr(847), end='')
            telefone = input("TELEFONE: ")

        print(chr(847), end='')
        logo = input("LOGOTIPO: ")
        # while not funcionalidades.valida_cadastro(cadastro):
          #  print(chr(847), end='')
          #  cadastro = input("CNPJ: ")

        return (cadastro, razao, fantasia, endereco, cidade, bairro, cep, uf, email, url, logo, telefone)

if __name__ != "__main__":
    try:
        with open('loja.vdc', 'rb') as lojaconfig:
            Loja = pickle.load(lojaconfig)
    except FileNotFoundError:
        cadastro, razao, fantasia, endereco, cidade, bairro, cep, uf, email, url, logo, telefone = Loja.configurar_loja()
        loja = Loja(cadastro, razao, fantasia, endereco, cidade, bairro, cep, uf, email, url, logo, telefone)
        print("\nLoja Cadastrada com Sucesso!\n")

>>>>>>> origin/master
