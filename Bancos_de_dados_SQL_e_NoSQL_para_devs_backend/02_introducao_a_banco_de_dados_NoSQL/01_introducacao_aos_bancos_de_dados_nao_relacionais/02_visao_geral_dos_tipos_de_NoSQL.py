"""
    Tipos
    - Key-Value
    - Document
    - Coluna
    - Grafos
    - Entre Outros...

    Key-Value > Chave Valor
        - Armazena dados como pares de chave e valor, onde cada
        chave é um identificado único para acessar o valor correspondente.

        Exemplo de SGDB: Redis, Riak, Amazon DynamoDB

        Uso: Um site pode usar um banco de dados Redis para armazenar
        informações de sessão de usuário.

    Document
        - Armazenam dados em documentos semiestruturados, geralmente em
        formato JSON ou BSON.

        Exemplo de SGBD: MongoDB, Couchbase, Apache CouchDB

        Uso: Um catálogo de e-commerce pode usar o MongoDB para armzenar
        informações de produtos, como nome, descrição, preço e atributos
        adicionais.

    Coluna
        - Armazenam dados em formato de colunas, o que permite alta
        escalabilidade e eficiência em determinados tipos de consultas.

        Exemplo de SGBD: Apache Cassandra, ScyllaDB, HBase

        Uso: Um sistema de registro de aplicativos pode usar o Apache
        Cassandra para armazenar registros de log.

    Grafo
        - Armazenar e consultar dados interconectados, onde os relacionamentos
        entre os dados são tão importantes quanto os pŕoprios dados.

        Exemplo de SGBD: Neo4j, Amazon Neptune, JanusGraph

        Uso: Uma rede social pode usar o Neo4j para armazenar os perfils
        dos usuários e suas conexões, permitindo consultas eficientes para
        encontrar amigos em comum.
"""