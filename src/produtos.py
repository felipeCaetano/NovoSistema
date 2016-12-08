class Categoria(object):
    def __init__(self, codigo, nome, descricao):
        self._codigo = codigo
        self._nome = nome
        self._descricao = descricao

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @codigo.deleter
    def codigo(self):
        del self._codigo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @nome.deleter
    def nome(self):
        del self._nome

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    @descricao.deleter
    def descricao(self):
        del self._descricao

    # overrides magic methods

    

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.codigo == other.codigo


class Subcategoria(Categoria):
    def __init__(self, categoria, codigo, nome, descricao):
        self.cat = categoria
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao


class Produtos(object):
    """
    Classe Produtos: Modela produtos a serem comercializados
    Produto apresenta atributos relativos a caracterização e descrição de um produto
    >Impelementados: Inicializador, getters, setters e validadores
    """
    def __init__(self, subcategoria, codigo, nome, descricao, estoquemax, estoquemin, quantidade, valorvenda, valorcompra, foto):
        self._sub = subcategoria
        self._codigo = codigo
        self._nome = nome
        self._foto = foto
        self._descricao = descricao
        self._estoquemax = estoquemax
        self._estoquemin = estoquemin
        self._quantidade = quantidade
        self._vbvenda = valorvenda
        self._vbcompra = valorcompra

# properties

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @nome.deleter
    def nome(self):
        del self._nome

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self.codigo = value

    @codigo.deleter
    def codigo(self):
        del self.codigo

    @property
    def foto(self):
        return self._foto

    @foto.setter
    def foto(self, value):
        self.foto = value

    @foto.deleter
    def foto(self):
        del self._foto

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self.descricao = value

    @descricao.deleter
    def descricao(self):
        del self._descricao

    @property
    def estoquemax(self):
        return self._estoquemax

    @estoquemax.setter
    def estoquemax(self, value):
        while not self.valida_estoque(value):
            print("Quantidade Inválida")
            value = input("ESTOQUE MAX: ")
        else:
            self._estoquemax = value

    @estoquemax.deleter
    def estoquemax(self):
        del self._estoquemax

    @property
    def estoquemin(self, value):
        return self._estoquemin

    @estoquemin.setter
    def estoquemin(self, value):
        while not self.valida_estoque(value):
            print("Quantidade Inválida")
            value = input("ESTOQUE MIN: ")
        else:
            self._estoquemin = value

    @estoquemin.deleter
    def estoquemin(self):
        del self._estoquemin

    @property
    def vbvenda(self):
        return self._vbvenda

    @vbvenda.setter
    def vbvenda(self, value):
        while not self.valida_valorvenda(value):
            print("Valor Inválid0")
            value = input("Valor de Venda: ")
        else:
            self._vbvenda = value

    @vbvenda.deleter
    def vbvenda(self):
        del self._vbvenda

    @property
    def vbcompra(self):
        return self._vbcompra

    @vbcompra.setter
    def vbcompra(self, value):
        pass

    @vbcompra.deleter
    def vbcompra(self):
        pass

# validadores
    @staticmethod
    def valida_estoque(value):
        if value == "":
            return False
        if not value.isdigit():
            return False
        elif int(value) <= 0:
            return False
        else:
            try:
                int(value)
                return True
            except:
                return False

    @staticmethod
    def valida_valorvenda(value):
        if value == "":
            print("String Vazia")
            return False
        else:
            value=value.replace(",",".")    # se virgula for digitada no lugar de ponto
            if value <= '0':
                print("String negativa")
                return False
            else:
                try:
                    float(value)
                    return True
                except:
                    print("String falha na conversão")
                    return False

    def __str__(self):
        return str(self.__dict__)