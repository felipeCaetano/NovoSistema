# -*- coding: utf-8 -*-
import os
import getpass
from datetime import datetime

import funcionalidades
from Vendas import Vendas
from Estoque import Estoque
from Pessoas import Pessoas
from Loja import *


def main_menu(vendas, estoque, pessoas, acess, nome, cargo):
    os.system("cls")
    while 1:
        print(chr(164) * 18, "- SISTEMA DE VENDA AO CONSUMIDOR -", chr(164) * 18)
        print("Nome:",Loja.fantasia.ljust(1), end="")
        print("CNPJ: ".rjust(40),(Loja.cadastro))

        funcionalidades.get_weekday()
        print("Usuário:" , nome.ljust(15), end=" ")
        print("Acesso: ".rjust(52-(len(nome)+8)), cargo)
        print(chr(164) * 18, "- MENU INICIAL -".center(34), chr(164) * 18)
        # pegando a data:

        print("\nESCOLHA A FUNÇÃO:\n1- VENDER","5- CONTROLE DE PESSOAL".rjust(60),"\n2- COMPRAR",
              "6- CONTROLE DE ESTOQUE".rjust(59),"\n3- RELATORIO DE VENDAS","7- LOJA".rjust(32),
              "\n4- RELATORIO DE COMPRAS","8- AJUDA".rjust(32),"\n0- SAIR")
        op = input()
        while not funcionalidades.valida_opcao(op, "012345678"):
            print("Opção Inválida!\n")
            op = input()
        op = int(op)
        if op == 1:
            vendas.vender(estoque, pessoas)
        elif op == 0:
            os.system('cls')
            break

        if acess:
            if op == 2:
                vendas.comprar(estoque, pessoas)
            elif op == 3:
                vendas.relatorio_venda()
            elif op == 4:
                vendas.relatorio_compra()
            elif op == 5:
                pessoas.menu_pessoas()
            elif op == 6:
                estoque.menu_estoque()
        else:
            print("Menu Indisponível! -> Você não tem privilégios suficientes.")

def login(pessoas):
    cargo =""
    os.system("cls")
    print(chr(164) * 18, "Tela de LOGIN:", chr(164) * 18)
    while 1:
        username = input("USUÁRIO: ")
        password = getpass.getpass("SENHA: ")

        if username == "admin" and password == "admin":
            return (True, "Administrador", "Administrador")
        else:
            for funcionario in pessoas.funcionarios:
                print("Verificando nivel de acesso para %s" % funcionario.nome)
                print("%s" % funcionario.gerente)
                if funcionario.login == username:
                    if funcionario.password == password:
                        acess = funcionario.gerente
                        if acess:
                            cargo = "Gerente"
                        else:
                            cargo = "Funcionário"

                    return (acess, funcionario.nome, cargo)
            else:
                print("ATENÇÃO! Usuário/Senha Inválido.", file = warning)

def main():

    v = Vendas()
    e = Estoque()
    p = Pessoas()

    acess, nome, cargo = login(p)
    main_menu(v, e, p, acess, nome, cargo)  # colocar atributo de acesso.

if __name__ == "__main__":
    main()
