#!/usr/bin/python
# _*_ coding: utf-8 _*_
# Cadastro de clientes, fornecedores e funcionários

LOGINMAXLENGTH = 9


class Pessoa(object):
    def __init__(self, nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro):
        self.__nome = nome
        self.__endereco = end
        self.__numero = num
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__cep = cep
        self.__estado = uf
        self.__telefone = tel
        self.__celular = cel
        self.__email = email
        self.__rg = rg
        self.__cadastro = cadastro
        self.ativo = False

# metodos getters e setters

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        while not self.valida_nome(valor):
            print("Nome Inválido")
            valor = input("NOME COMPLETO: ")
        else:
            self.__nome = valor

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, valor):
        while not self.valida_endereco(valor):
            print("Endereço Inválido")
            valor = input("ENDEREÇO: ")
        else:
            self.__endereco = valor

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):
        while not self.valida_numero(valor):
            print("Número Inválido")
            valor = input("NÚMERO: ")
        else:
            self.__numero = valor

    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, valor):
        self.__complemento = valor

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, valor):
        while not self.valida_bairro(valor):
            print("Bairro Inválido")
            valor = input("BAIRRO: ")
        else:
            self.__bairro = valor

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, valor):
        while not self.valida_cidade(valor):
            print("Cidade Inválida")
            valor = input("CIDADE: ")
        else:
            self.__cidade = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        while not self.valida_estado(valor):
            print("Estado Inválido")
            valor = input("UF: ")
        else:
            self.__estado = valor

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, valor):
        while not self.valida_telefone(valor):
            print("Telefone Inválido")
            valor = input("TELEFONE: ")
        else:
            self.__telefone = valor

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, valor):
        while not self.valida_celular(valor):
            print("Celular Inválido")
            valor = input("CELULAR: ")
        else:
            self.__celular = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        while not self.valida_email(valor):
            print("Email Inválido")
            valor = input("EMAIL: ")
        else:
            self.__email = valor

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, valor):
        while not self.valida_rg(valor):
            print("RG Inválido")
            valor = input("RG: ")
        else:
            self.__rg = valor

    @property
    def cadastro(self):
        return self.__cadastro

    @cadastro.setter
    def cadastro(self, valor):
        while not self.valida_cadastro(valor):
            print("CPF\CNPJ Inválido")
            valor = input("Cadastro(CPF ou CNPJ): ")
        else:
            self.__cadastro = valor

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, valor):
        while not self.valida_cep(valor):
            print("CEP Inválido")
            valor = input("CEP: ")
        else:
            self.__cep = valor

    # validadores Estáticos - Invocados antes de instanciarmos objetos para evitar instancias erradas
    @staticmethod
    def valida_nome(nome):
        if nome is "":
            print("Nome Invalido! ", end="")
            print("Nome NÃO pode ser em branco!")
            return False
        n = nome.split()
        for c in n:
            if not c.isalpha():
                print("Nome Invalido! ", end="")
                print("NOME DEVE CONTER APENAS LETRAS!")
                return False
        else:
            return True

    @staticmethod
    def valida_endereco(endereco):
        if endereco == "":
            return True
        end = endereco.strip()
        end = end.split()
        if end[0] not in ['Al.', 'Alameda', 'Rua', 'Dsc.', 'Descida', 'Aveninda', 'R.', 'Av.', 'Ld.', 'Ladeira',
                          'Estrada', 'Travessa', 'Trav.', 'Est.', 'Beco']:
                print("Inisira LOGRADOURO VÁLIDO!")
                print(sorted(['Al.', 'Alameda', 'Rua', 'Dsc.', 'Descida', 'Aveninda', 'R.', 'Av.', 'Ld.', 'Ladeira',
                              'Estrada', 'Travessa', 'Trav.', 'Est.', 'Beco']))
                return False
        else:
            return True

    @staticmethod
    def valida_numero(numero):
        nb = numero.strip()
        if nb == "" or nb == "S/N":
            return True
        if not nb.isdigit():
            print("Valor deve ser númerico ou S/N!")
            return False
        else:
            return True

    @staticmethod
    def valida_bairro(bairro):
        if bairro == "":
            return True
        b = bairro.strip()
        b = b.split()
        if not b[0].isalpha():
            print("Bairro Deve ter NOME começado com palavra!")
            return False
        else:
            return True

    @staticmethod
    def valida_cidade(cidade):
        if cidade == "":
            return True
        for city in cidade.strip().split():
            if not city.isalpha():
                print("Cidade Deve ter NOME começado com palavra!")
                return False
        else:
            return True

    @staticmethod
    def valida_estado(estado):
        estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG',
                   'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        e = estado.strip()
        if e.upper() not in estados:
            print("Digite UF do BRASIL Válida!")
            return False
        else:
            return True

    @staticmethod
    def valida_cep(cep):
        if cep == "":
            return True
        c = cep.replace("-", "")
        if len(c) != 8:
            print("CEP Inválido! Verifique a quantidade de dígitos")
            return False
        elif c.isdigit():
            return True

    @staticmethod
    def valida_telefone(telefone):
        # TODO: verificar os DDDs se estão de acordo com a lista do Brasil
        s = telefone
        s = s.replace("(", "")
        s = s.replace(")", "")
        s = s.replace("-", "")

        if telefone == "":
            return True
        elif len(s) < 8:
            print("Telefone Inválido! Verifique a quantidade de dígitos")
            return False
        elif 8 < len(s) <= 10 and s.isdigit():
            return True

    @staticmethod
    def valida_celular(celular):
        s = celular.replace("(", "")
        s = celular.replace(")", "")
        s = celular.replace("-", "")
# TODO: verificar os DDDs se estão de acordo com a lista do Brasil
        if celular == "":
            return True
        if len(s) < 9:
            print("Celular Inválido! Numero de digitos Inválidos!")
            return False
        if len(s) == 9 and s[0] != '9':
            print("Celular Inválido! Numero deve começar por 9!")
            return False
        if len(s) == 11 and s[2] != '9':
            print("Celular Inválido! Numero deve começar por 9!")
            return False
        else:
            return True

    @staticmethod
    def valida_email(email):
        """Verificador de email fraco
        @TODO - Usar expressões regulares
        verifica apenas se tem @ e .com
        """
        if email != "":
            pos = email.find('@')
            if pos > 0:
                if email.find(".com") > 0:
                    return email
                else:
                    print("EMAIL inválido! Insira a terminação .com")
                    return False
            else:
                print("EMAIL inválido! Não deve começar por @")
                return False
        else:
            print("EMAIL inválido! Endereço deve conter @")
            return False

    @staticmethod
    def valida_rg(rg):
        if rg == "":
            return True
        if 5 <= len(rg) <= 7:
            if rg.isdigit():
                return True
            else:
                print("RG Inválido! Valor deve ser numérico")
                return False
        else:
            print("RG Inválido! Verifique a quantidade de Dígitos")
            return False

    @staticmethod
    def valida_cadastro(cadastro):
        result = 0
        s = cadastro
        s = s.replace("-", "")  # remove o traço se houver
        s = s.replace(".", "")
        s = s.replace("/", "")

        if len(s) < 11:
            print("CPF/CNPJ Inválido! Verifique a quantidade de Dígitos")
            return False  # maior ou menor q 11 n vale 012923084-78
        if len(s) == 11:
            a = [int(x) for x in range(2, 11)]
            a.reverse()  # primeira parte da vericação
            for i in range(9):
                result += int(s[i]) * a[i]

            result = (result * 10) % 11
            if result == 10:  # se resto da divisão for 10
                result = 0

            if result == int(s[9]):  # verificação 1 ok.
                result = 0
                b = [int(x) for x in range(2, 12)]
                b.reverse()
                for i in range(10):
                    result += int(s[i]) * b[i]

                result = (result * 10) % 11
                if result == int(s[10]):  # verificação 2 ok.
                    return True
                else:
                    print("CPF Inválido! Erro no digito Verificador")
                    return False
            else:
                print("CPF Inválido! Erro no digito Verificador")
                return False

        elif len(s) == 14:
            lista = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            resultado = 0
            for i in range(12):
                resultado += lista[i] * int(s[i])
            resultado %= 11

            if resultado < 2:
                resultado = 0
            else:
                resultado = 11 - resultado

            if resultado == int(s[12]):
                lista = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
                resultado = 0
                for i in range(13):
                    resultado += lista[i] * int(s[i])

                resultado %= 11

                if resultado < 2:
                    resultado = 0
                else:
                    resultado = 11 - resultado

                if resultado == int(s[13]):
                    return True
                else:
                    print("CNPJ Inválido! Erro no digito Verificador")
                    return False
            else:
                print("CNPJ Inválido! Erro no digito Verificador")
                return False

    def __str__(self):
        return str(self.__dict__)


class Cliente(Pessoa):

    def __init__(self, nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro, datanasc):
        Pessoa.__init__(self, nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro)
        self.__datanasc = datanasc
        self.ativo = False

    @property
    def datanasc(self):
        return self.__datanasc

    @datanasc.setter
    def datanasc(self, valor):
        while not self.valida_data(valor):
            print("Data Inválida")
            valor = input("DN(dd/mm/aaaa): ")
        else:
            self.__datanasc = valor

    @staticmethod
    def valida_data(data):
        s = data.replace("/", "")
        if data == "":
            return data
        else:
            if int(s[0:2]) > 31:
                return False
            if int(s[2:4]) > 12:
                return False
            # TODO:se ano maior q ano atual tb deve retornar False - Testar em funcionalidades

            if len(s) == 8 and s.isdigit():
                return True
            else:
                return False


class Fornecedor(Pessoa):
    # fornecedor tem cnpj
    def __init__(self, nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, cadastro):
        super(Fornecedor, self).__init__(nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, 111111,
                                         cadastro)


class Funcionario(Pessoa):
    logins_list = []

    def __init__(self, nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro, datanasc,
                 gerente, foto):
        super(Funcionario, self).__init__(nome, end, num, complemento, bairro, cidade, cep, uf, tel, cel, email, rg,
                                          cadastro)
        self.__datanasc = datanasc
        self.__login = self.create_login(nome)
        self.__password = self.set_password()
        self.__gerente = gerente
        self.__foto = foto

# metodos exclusivos dos funcinários: Login e Senha

    def create_login(self, nome):
        """
        Cria um login para um funcionário no momento do seu registro. Cada login de funcionário deve ser unico e criado
        apartir do seu nome fornecido.

        O login tem um numero fixo de caracteres e é formado pelas iniciais dos primeiros nomes + o ultimo nome desde
        não ultrapasse o tamanho fixado

        :param nome: nome do funcionário
        :return: LOGIN do funcionário
        """

        login = ""
        lista = nome.split()

        for i, n in enumerate(lista):
            if i == len(lista)-1:
                if len(n) > 3:
                    login += n
            else:
                if len(n) > 3:
                    login += n[0]
            login = login.lower()
        if len(login) > LOGINMAXLENGTH:
            login = login[:-(len(login)-LOGINMAXLENGTH)]
        print("Seu LOGIN é: ", login)
        return login

    def set_password(self):
        """
        Metodo para solicitar e salvar senha do funcionário.
        Senha deve ser digitada duas vezes e deve ser igual e de 8 caracteres

        :return: senha do usuário
        """

        senha1 = ""
        while not len(senha1) == 8:
            print("Defina sua SENHA com 8 caracteres:\n")
            senha1 = input("Digite sua senha: ")
            senha2 = input("Repita sua senha: ")
            if len(senha1) != len(senha2):
                print("As senhas devem ter 8 caracteres!")
                senha1 = ""
        while not senha1 == senha2:
            print("As senhas devem ser iguais!\n")
            senha1 = input("Digite sua senha: ")
            senha2 = input("Repita sua senha: ")
        else:
            return senha1

    @property
    def datanasc(self):
        return self.__datanasc

    @datanasc.setter
    def datanasc(self, valor):
        while not self.valida_data(valor):
            print("Data Inválida")
            valor = input("DN(dd/mm/aaaa): ")
        else:
            self.__datanasc = valor

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def gerente(self):
        return self.__gerente

    # Validadores estáticos de Funcionários
    @staticmethod
    def valida_data(data):
        s = data.replace("/", "")
        if data == "":
            return data
        else:
            if int(s[0:2]) > 31:
                return False
            if int(s[2:4]) > 12:
                return False
            # TODO:se ano maior q ano atual tb deve retornar False
            if len(s) == 8 and s.isdigit():
                return True
            else:
                return False

    @staticmethod
    def valida_status(gerente):

        if gerente == "":
            print("Status ERROR - Deve ser fornecido o nivel de acesso ao sistema!")
            return False
        else:
            if gerente.lower() == 's' or gerente.lower() == 'sim' or gerente.lower() == 'n' or gerente.lower() == 'nao'\
                    or gerente.lower() == 'não':
                return True
            else:
                print("Opção Inválida! Digite Somente S ou N")
                return False
