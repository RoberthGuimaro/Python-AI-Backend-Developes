"""
    Porque precisamos manipular arquivos?
    - Para manipular arquivos em Python, primeiro precisamos abri-los.
    Usamos a função 'open()' para isso. Quando terminamos de trabalhar
    com o arquivo, usamos a função 'close()' para liberar recursos.

    exemplo de codigo:

file = open("example.txt", "r")
fazemos algo com o arquivo...
file.close()
"""

"""
    Modos de abertura de arquivo
    - Existem diferentes modos para abrir um arquivo, como
    somente leitura ('r'), gravação ('w') e anexar ('a').
    O modo de abertura deve ser escolhido de acordo com a
    operação que iremos realizar no mesmo.

    Exemplo de código:

Para ler um arquivo
file = open('example.txt', 'r')

Para escrever em um arquivo
file = open('example.txt', 'w')

Para anexar conteúdo a um arquivo existente
file = open('example.txt', 'a')
"""