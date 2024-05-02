"""
    Problema:
    id   nome    endereco
    1    Joao    Rua A, 123, Cidade X, Estado Y
    2    Maria   Rua B, 456, Cidade Y, Estado Z
    3    Pedro   Avenida C, 789, Cidade X, Estado Y

    Como buscar todos os usuários da Cidade X?

    Normalização de dados
    - A normalização de dados é um processo no qual se
    organiza e estrutura um banco de dados relacional de
    forma e eliminar redundâncias e anomalias, garantindo a
    consistência e integridade dos dados.

    Formas normais
    - 1FN: Atomicidade de dados
        A 1FN estabelece que cada valor em uma tabela deve ser
        atômico, ou seja, indivisível. Nenhum campo deve conter
        múltiplos valores ou listas. No seu caso, o campo
        "endereco" contém múltiplos valores, como rua, número, cidade
        e estado. Para atingir a 1FN, precisamos dividir o campo
        "endereco" em colunas separadas.

    - 2FN:
        A 2FN estabelece que uma tabela deve estar na 1FN.
        Todos os atributos não chave devem depender totalmente da
        chave primária.

        Dica se sua tabela tem uma chave primária simples não existe
        a possibilidade de termos dependência parcial e por tanto ela
        já se encontra na 2FN.

    - 3FN:
        Uma tabela deve estar na 2FN.
        Nenhuma coluna não-chave depender de outra coluna
        não-chave.
        
        Nosso exemplo: Relação ESTADO -> CIDADE

    Resumo
        - A 1FN garante que cada valor seja atômico e que os registro
        sejam únicos e identificáveis.

        - A 2Fn garante que os atributos não chave dependam totalmente
        da chave primária, evitando dependências parciais.

        - A 3FN elimina dependências transitivas entre os atributos
        não chave, garantindo que cada atributo não chave dependa
        apenas da chave primária, não havendo dependências indiretas
        entre eles.
"""