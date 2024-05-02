"""
    Tabelas
    - Ela é usada para armazenar dados de forma organizada.
    Cada tabela em um banco de dados relacional tem um nome
    único e é dividida em colunas e linhas.

    Colunas
    - Uma coluna é uma estrutura dentro de uma tabela que
    representa um atributo específico dos dados armazenados.
    Cada Coluna tem um nome único e um tipo de dados associado
    que define o tipo de informação que pode ser armazenado
    nela, como números, textos, datas, etc.

    Registros
    - Um registro, também é conhecido como linha ou tupla, é uma
    intância individual de dados em uma tabela.

    Comando: CREATE TABLE

    CREATE TABLE {{nome}}
    
        ({{coluna}}{{tipo}}{{opcoes}} COMMENT {{'comentario'}});


    Tipos de dados
    - Os dados podem variar muito entre os diversos SGBD, os mais
    comuns são:
        - inteiro (integer)
        - Decimal/Numerico (Decimal/Numeric)
        - Caractere/Varchar (Character/Varchar)
        - Data/Hora (Date/Time)
        - Booleano (Boolean)
        - Texto longo (text)

    Opcoes
    - Restrições de valor
        - NOT NULL
        - UNIFIQUE
        - DEFAULT
    - Chaves primárias e estrangeiras
    - Auto incremento

"""