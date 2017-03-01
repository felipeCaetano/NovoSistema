import re           # expressões regulares
import sys
from datetime import datetime

warning = sys.stderr


def valida_opcao(opcao, options):
    if opcao.isdigit() and opcao in options:
        return True
    else:
        return False

# TODO: Trocar Validadores por Expressões Regulares


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

    if re.match(cpf, cadastro):

        cpf = sum([int(x) for x in s])
        if cpf == 33 or cpf == 44 or cpf == 55:
            return True
        else:
            print("CPF Invalido! -> Verifique sequencia digitada.")
            return False

    elif re.match(cnpj, cadastro):

        lista = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        for i, p in enumerate(lista):
            result += p * int(s[i])
        result %= 11

        if result < 2:
            result = 0
        else:
            result = 11 - result

        if result == int(s[12]):
            lista = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            result = 0
            for i, p in enumerate(lista):
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


def valida_cidade(cidade):
    if cidade == "":
        return True
    for city in cidade.strip().split():
        if not city.isalpha():
            print("Cidade Deve ter NOME começado com palavra!")
            return False
    else:
        return True


def valida_estado(estado):
    estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG',
               'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    e = estado.strip()
    if e.upper() not in estados:
        print("Digite UF do BRASIL Válida!")
        return False
    else:
        return True


def valida_cep(cep):
    if re.match(r'\d{5}.*\d{3}', cep) or cep == "":
        return True
    else:
        print("CEP Inválido! -> Verifique os números digitados")
        return False


def valida_email(email):
    if re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return True
    else:
        print("Email Inválido! -> Verifique o email digitado.")
        return False


def valida_url(url):
    if re.match(r'[^@]+\.com\.+', url):
        return True
    else:
        print("A regex tá errada")
        return False


def valida_telefone(telefone):
    if re.match(r'.*\d{2}.*\d{4}.*\d{4}', telefone):
        return True
    else:
        print("A regex tá errada")
        return False


def valida_data ( data ):
    year = datetime.now().year

    s = data.replace("/", "")
    if data == "":
        return data
    else:
        if int(s[0:2]) > 31:
            print("ATENÇÃO! Data inválida.")
            # TODO verificar codigos para meses q tem menos dias.
            return False
        if int(s[2:4]) > 12:
            return False
        if int(s[4:8]) > int(year):
            print("ATENÇÃO! - Ano não pode ser o ano atual.", file=sys.stderr)
            return False
        if len(s) == 8 and s.isdigit():
            return True
        else:
            print("ATENÇÃO! - Data inválida")
            return False


def remove_caracter(dado):
    '''
    Remove os caracteres utilizados na formatação de telefones, cpfs, cnpj
    que são utilizados para melhor vizualização em consulta

    :param dado: entrada a ser removidos os caracteres como . - /
    :return: dado sem os caracteres
    '''
    dado = dado.replace("-", "")  # remove o traço se houver
    dado = dado.replace(".", "")
    dado = dado.replace(" ", "")
    dado = dado.replace("/", "")

    return dado


def get_weekday():
    today = datetime.now().strftime("%d/%m/%Y - %H:%M")
    dia = datetime.now().weekday()

    if dia == 6:
        print("Domingo, ", end="")
    elif dia == 0:
        print("Segunda-feira, ", end="")
    elif dia == 1:
        print("Terça-feira, ", end="")
    elif dia == 2:
        print("Quarta-feira, ", end="")
    elif dia == 3:
        print("Quinta-feira, ", end="")
    elif dia == 4:
        print("Sexta-feira, ", end="")
    elif dia == 5:
        print("Sábado, ", end="")

    print(today, end="\n")
