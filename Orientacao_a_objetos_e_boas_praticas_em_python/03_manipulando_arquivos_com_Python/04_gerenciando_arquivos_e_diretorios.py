"""
    Gerenciando arquivos e diretórios
    - Python também oferece funções para gerenciar arquivos e
    diretórios. Podemos criar, renomear e excluir arquivos e 
    diretórios usando os módulos 'os' e 'shutil'.

    Exemplo de código:

import os
import shutil

Criar um diretório
os.mkdir('exemplo')

Renomear um arquivo
os.rename('old.txt', 'new.txt')

Remover um arquivo
os.remove('unwanted.txt')

Mover um arquivo
shtuil.move('source.txt', 'destination.txt')
"""

import os
import shutil
from pathlib import Path

# pegando o caminho da pasta
ROOT_PATH = Path(__file__).parent

# criando o diretorio na pasta do root_path
# os.mkdir(ROOT_PATH / 'novo-diretorio')

# criando arquivo na pasta do root_path
# arquivo = open(ROOT_PATH / 'novo.txt', 'w')
# arquivo.close()

# renomeando o arquivo na pasto do root_path
# os.rename(ROOT_PATH/'novo.txt', ROOT_PATH/'renomeado.txt')

# Removendo um arquivo do diretorio root_path
# os.remove(ROOT_PATH / 'renomeado.txt')

# Movendo um arquivo do diretorio root_path para o diretorio 'novo-diretorio'
# shutil.move(ROOT_PATH / 'novo.txt', ROOT_PATH / 'novo-diretorio' / 'novo.txt')