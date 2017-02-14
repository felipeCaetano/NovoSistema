from datetime import datetime

from funcionalidades import valida_opcao
from Vendas import Vendas

from Estoque import Estoque

from Pessoas import Pessoas
from Loja import *


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


def main_menu(vendas, estoque, pessoas):
    while 1:
        print(chr(847) * 18, "- SISTEMA DE VENDA AO CONSUMIDOR -", chr(847) * 18)
        print(chr(847) * 18, "- MENU INICIAL -".center(34), chr(847) * 18)
        # pegando a data:
        get_weekday()
        print("\nESCOLHA A FUNÇÃO:\n1- VENDER\t\t\t\t\t\t5- CONTROLE DE PESSOAL\n2- COMPRAR\t\t\t\t\t\t"
              "6- CONTROLE DE ESTOQUE\n3- RELATORIO DE VENDAS\t\t\t7- LOJA\n4- RELATORIO DE COMPRAS\t\t\t8- AJUDA\n"
              "0- SAIR")
        op = input()
        while not valida_opcao(op, "012345678"):
            print("Opção Inválida!\n")
            op = input()
        if op == '1':
            vendas.menu_vendas(estoque, pessoas)
        elif op == '2':
            vendas.comprar(estoque, pessoas)
        elif op == '3':
            vendas.relatorio_venda()
        elif op == '4':
            vendas.relatorio_compra()
        elif op == '5':
            pessoas.menu_pessoas()
        elif op == '6':
            estoque.menu_estoque()
        elif op == '0':
            break
        else:
            print("Escolheu outra coisa")


def main():

    v = Vendas()
    e = Estoque()
    p = Pessoas()


    main_menu(v, e, p)

if __name__ == "__main__":
    main()
