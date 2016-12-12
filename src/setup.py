"""
Arquivo necessário para distribuição
"""
from distutils.core import setup

setup(
    name = 'Sistema de Vendas Direta',
    version = '1.0.0',
    py_modules = ['clientes', 'Estoque', 'produtos', 'Vendas'],
    author = 'felipeCaetano e Monica Alves',
    author_email = 'felipecmelo@gmail.com',
    url = None,
    description = 'Um simples de programa de vendas e controle de estoque.'
)