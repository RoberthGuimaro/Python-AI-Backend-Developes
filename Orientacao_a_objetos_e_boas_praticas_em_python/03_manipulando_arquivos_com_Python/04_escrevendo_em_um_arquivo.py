"""
    Escrevendo em um arquivo
    - Podemos usar 'write()' ou 'writelines()' para escrever em um
    arquivo. Lembre-se, no entanto, de abrir o arquivo no modo correto.
"""

arquivo = open('/home/roberth/Documents/GitHub/Python-AI-Backend-Developes/Orientacao_a_objetos_e_boas_praticas_em_python/03_manipulando_arquivos_com_Python/teste.txt', 'w')
arquivo.write('Escrevendo dados em  um novo arquivo.')
arquivo.writelines(['\n','Escrevendo', ' um', ' novo', ' texto'])
arquivo.close()