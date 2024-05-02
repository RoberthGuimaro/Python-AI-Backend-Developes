"""
    Análise do Plano de Execução
        - Ela nos permite examinar as operações realizadas, as tabelas
        acessadas, os índices utilizados e outras informações importantes
        para identificar possíveis melhorias de desempenho.

    Comandos:
        - EXPLAIN
            SELECT * FROM {{TABELA}}

    - select_type: "SIMPLE", "SUBQUERY", "JOIN"
    - table
    - type: "ALL", "INDEX", entre outros
    - possible_keys: Os índices possíveis que podem ser utilizados na operação
    - key: O índice utilizado na operação, se aplicável
    - key_len: O comprimento do índice utilizado
    - ref: As colunas ou constantes usadas para acessar o índice
    - rows

    Índices de Busca
    - Esses recursos são fundamentais para melhorar o desempenho das consultas
    e otimizar a recuperação de informações em bancos de dados.

        CREATE INDEX {{nome_index}}
        ON {{tabela}}{{coluna1, coluna2....}}
"""