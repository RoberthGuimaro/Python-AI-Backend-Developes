"""
    Introdução
    - Vamos aprender sobre arquivos CSV, um formato de arquivo
    amplamente utilizado para armazenar dados tabulares. CSV é a
    sigla para 'Comma Separated Values'.

    Lendo arquivos CSV
    - Python oferece um módulo chamado 'csv' para lidar facilmente
    com arquivos CSV.

    Exemplo de código

import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

    Escrevendo em arquivos CSV
    - Da mesma forma podemos utilizar o módulo 'csv' para
    escrever em arquivos CSV.

    Exemplo de código

import csv

with open ('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nome', 'idade'])
    writer.writerow(['ana', 30])
    writer.writerow(['joao', 25])

    Práticas recomendadas
    - Usar csv.reader e csv.writer para manipular arquivos csv.

    - Fazer o tratamento correto das excessões.

    - Ao gravar arquivos CSV definir o argumento newline='' no metodo
    'open'.
"""

import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1

#try:
#    with open(ROOT_PATH / 'usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
#        escritor = csv.writer(arquivo)
#        escritor.writerow(['id', 'nome'])
#        escritor.writerow(['1', 'Roberth'])
#        escritor.writerow(['2', 'Larissa'])

#except IOError as exc:
#    print(f'Erro ao criar o arquivo. {exc}')

#try:
#    with open(ROOT_PATH / 'usuarios.csv', 'r', newline='', encoding='utf-8') as arquivo:
#        leitor = csv.reader(arquivo)
#        for idx, row in enumerate(leitor):
#            if idx == 0:
#                continue
#            print(f'ID: {row[COLUNA_ID]}')
#            print(f'Nome: {row[COLUNA_NOME]}')

#except IOError as exc:
#    print(f'Erro ao criar o arquivo. {exc}')

try:
    with open(ROOT_PATH / 'usuarios.csv', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        for row in leitor:
            print(f'ID: {row["id"]}')
            print(f'Nome: {row["nome"]}')

except IOError as exc:
    print(f'Erro ao criar o arquivo. {exc}')