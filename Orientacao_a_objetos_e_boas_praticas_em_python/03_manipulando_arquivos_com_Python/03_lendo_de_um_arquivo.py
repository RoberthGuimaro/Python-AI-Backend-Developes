"""
    Lendo de um arquivo
    - Python oferece várias maneiras de ler um arquivo.
    Podemos usar 'read()', 'readline()' ou 'readlines()'
    dependendo de nossas necessidades.
"""

"""
    Método read
    - Ler todo o conteúdo do arquivo de uma vez.
    file = open('example.txt', 'r')
    print(file.read())
    file.close()
"""

"""
    Método readline e readlines
    - O Método 'readline()' lê uma linha por vez,
    enquanto 'readlines()' retorna uma lista onde
    cada elemento é uma linha do arquivo.
"""

arquivo = open('/home/roberth/Documents/GitHub/Python-AI-Backend-Developes/Orientacao_a_objetos_e_boas_praticas_em_python/03_manipulando_arquivos_com_Python/lorem.txt', 'r')
print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

# tip
# while len(linha := arquivo.readline()):
#    print(linha)

arquivo.close()