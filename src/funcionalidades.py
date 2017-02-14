import re           # expressões regulares

def valida_opcao(opcao, options):
    if opcao.isdigit() and opcao in options:
        return True
    else:
        return False


def valida_nome(nome, type):
    if type == "pessoa":
        if nome is "":
            print("Nome Invalido! -> NÃO pode ser em branco!")
            return False
        n = nome.split()
        for c in n:
            if not c.isalpha():
                print("Nome Invalido! -> NOME DEVE CONTER APENAS LETRAS!")
                return False
        else:
            return True
    elif type == "loja":
        if nome is "":
            print("Razão Social Invalida! -> NÃO pode ser em branco!")
            return False
        n = nome.split()
        for c in n:
            if not c.isalpha():
                print("Nome Invalido! -> NOME DEVE CONTER APENAS LETRAS!")
                return False
        else:
            return True

def valida_cadastro(cadastro):

    cpf = re.compile(r'\d{3}.*\d{3}.*\d{3}.*\d{2}')
    cnpj = re.compile(r'\d{2}.*\d{3}.*\d{3}.*\d{4}.*\d{2}')
    result = 0

    s = cadastro
    s = s.replace("-", "")  # remove o traço se houver
    s = s.replace(".", "")
    s = s.replace(" ", "")
    s = s.replace("/", "")

    if re.match(cpf,cadastro):
        print("é cpf!")

        cpf = sum([int(x) for x in s])
        if cpf == 33 or cpf == 44 or cpf == 55:
            return True
        else:
            return False


    elif re.match(cnpj,cadastro):

        lista = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        for i,p in enumerate(lista):
            result += p * int(s[i])
        result %= 11

        if result < 2:
            result = 0
        else:
            result = 11 - result

        if result == int(s[12]):
            lista = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            result = 0
            for i,p in enumerate(lista):
                result += p * int(s[i])

            result %= 11

            if result < 2:
                result = 0
            else:
                result = 11 - result

            if result == int(s[13]):
                return True
            else:
                print("CNPJ Inválido! Erro no digito Verificador")
                return False
        else:
            print("CNPJ Inválido! Erro no digito Verificador")
            return False
    else:
        print("CPF/CNPJ Inválido! -> Verifique a quantidade de Dígitos")
        return False  # maior ou menor q 11 n vale 012923084-78
