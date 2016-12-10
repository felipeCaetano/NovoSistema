#!/usr/bin/python
# _*_ coding: utf-8 _*_
# Cadastro de clientes, fornecedores e funcionários


class Pessoa(object):
    def __init__(self, nome, end, num, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro):
        self.__nome = nome
        self.__endereco = end
        self.__numero = num
        self.__bairro = bairro
        self.__cidade = cidade
        self.__cep = cep
        self.__estado = uf
        self.__telefone = tel
        self.__celular = cel
        self.__email = email
        self.__rg = rg
        self.__cadastro = cadastro

# metodos getters e setters

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        while not self.valida_nome(valor):
            print("Nome Inválido")
            valor = input("NOME: ")
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

    # validadores
    def valida_nome(self, nome):
        if nome is "":
            Pessoa.__nome = input("NOME: ")
        n = nome.split()
        for c in n:
            if not c.isalpha():
                return False
        else:
            return nome

    def valida_endereco(self, endereco):
        end = endereco.strip()
        if end == "":
            return True
        for e in end:
            if not e.isalnum():
                return False
        else:
            return True

    def valida_numero(self, numero):
        nb = numero.strip()
        if nb == "":
            return True
        for number in nb:
            if not number.isdigit():
                return False
        else:
            return True

    def valida_bairro(self, bairro):
        b = bairro.strip()
        b = b.split()
        for nbh in b:
            if not nbh.isalpha():
                return False
        else:
            return True

    def valida_cidade(self, cidade):
        c = cidade.strip()
        c = cidade.split()
        for city in c:
            if not city.isalpha():
                return False
        else:
            return True

    def valida_estado(self, estado):
        estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG',
                   'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        e = estado.strip()
        if e.upper() not in estados:
            return False
        else:
            return True

    def valida_cep(self, cep):
        cep.replace("-", "")
        if len(cep) != 8:
            return False
        elif cep.isdigit():
            return True

    def valida_telefone(self, telefone):
        s = telefone.replace("(", "")
        s = telefone.replace(")", "")
        s = telefone.replace("-", "")

        if telefone == "":
            return True
        elif len(s) < 8:
            return False
        elif 8 < len(s) <= 10 and s.isdigit():
            return True

    def valida_celular(self, celular):
        s = celular.replace("(", "")
        s = celular.replace(")", "")
        s = celular.replace("-", "")

        if celular == "":
            return True
        if len(s) < 9:
            return False
        if len(s) == 9 and s[0] != '9':
            return False
        if len(s) == 11 and s[2] != '9':
            return False
        else:
            return True

    def valida_email(self, email):
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
                    return False
            else:
                return False
        else:
            return "Email Inválido"

    def valida_rg(self, rg):
        if rg == "":
            return True
        if rg != "":
            if 5 <= len(rg) <= 7:
                if rg.isdigit():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def valida_cadastro(self, cadastro):
        result = 0
        s = cadastro.replace("-", "")  # remove o traço se houver
        s = cadastro.replace(".", "")
        s = cadastro.replace("/", "")
        if len(s) < 11:
            return False  # maior ou menor q 11 n vale
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
                    return False
            else:
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
                    return False
            else:
                return False

    def __str__(self):
        return str(self.__dict__)


class Cliente(Pessoa):

    def __init__(self, nome, end, num, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro, datanasc):
        Pessoa.__init__(self, nome, end, num, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro)
        self.__datanasc = datanasc

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

    def valida_data(self, data):
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


class Fornecedor(Pessoa):
    # fornecedor tem cnpj
    def __init__(self, nome, end, num, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro):
        super(Fornecedor, self).__init__(nome, end, num, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro)


class Funcionario(Pessoa):
    # TODO: cliente tem foto
    logins_list = []

    def __init__(self, nome, end, num, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro, datanasc):
        super(Funcionario, self).__init__(nome, end, num, bairro, cidade, cep, uf, tel, cel, email, rg, cadastro)
        self.__datanasc = datanasc
        self.__login = self.create_login(nome)
        self.__pass = self.set_password()

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
        LOGINMAXLENGTH = 9
        login = ""
        cont = 0
        lista = nome.split()

        for i in range(len(lista)):
            if i == len(lista)-1:
                if len(lista[i]) > 3:
                    login += lista[i]
            else:
                if len(lista[i]) > 3:
                    login += lista[i][0]
            login = login.lower()
        if len(login) > LOGINMAXLENGTH:
            login = login[:-(len(login)-LOGINMAXLENGTH)]
        print("Seu LOGIN é: ", login)
        return  login

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

    def valida_data(self, data):
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

pessoa1 = Fornecedor("João", "ru", 12, "a", 'b', 52111200, 'PE', '34442125', '96360718', 'felipecmelo@gmail.com', '1234567', '01292308470')
print(pessoa1)
