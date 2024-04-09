"""
    Objetivo geral
        - Vamos aprender sobre iteradores e geradores Python.
        Esses são conceitos poderosos que nos permitem trabalhar
        com sequências de maneira eficiente.

    Introdução
        - Em Python, um iterador é um objeto que contém um número
        contável de valores que podem ser iterados, o que significa
        que você pode percorrer todos os valores. O protocolo do
        iterador é uma maneira do Python fazer a iteração de um
        objeto, que consiste em dois métodos especiais "__iter__()"
        e "__next__()".

    Ler arquivos grandes
        - Economiade memória, evitando carregar todas as linhas do
        arquivo.

        - Iterar linha a linha do arquivo.

"""


class MeuIterador:
    def __init__(self, numeros: list[list]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador] *2
            self.contador += 1
            return numero *2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[44, 22, 55]):
    print(i)