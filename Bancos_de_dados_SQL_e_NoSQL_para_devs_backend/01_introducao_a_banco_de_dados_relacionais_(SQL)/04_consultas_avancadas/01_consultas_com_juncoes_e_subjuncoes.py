"""
    Junções: JOINs
        - São usadas no SQL para combinar dados de duas ou mais 
        tabelas relacionadas em uma única consulta.

    Junções: Tipos
        - INNER JOIN
        - LEFT JOIN ou LEFT OUTER JOIN
        - RIGHT JOING ou RIGHT OUTER JOIN
        - FULL JOIN ou FULL OUTER JOIN

    INNER JOIN
        - Retorna apenas as linhas que têm correspondência em ambas
        as tabelas envolvidas na junção. A junção é feita com base em
        uma condição de igualdade especificada na cláusula ON.

        SELECT *

        FROM tabela1

        INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

    LEFT JOIN
        - Retorna todas as linhas da tabela à esquerda da junção e as
        linhas correspondentes da tabela à direita. Se não houver
        correspondência, os valores da tabela à direita serão NULL.

        SELECT *

        FROM tabela1

        LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

    RIGHT JOIN
        - Retorna todas as linhas da tabela à direita da junção e as linhas
        correspondentes da tabela à esquerda. Se não houver correspondência,
        os valores da tabela à esquerda serão NULL.

        SELECT *

        FROM tabela1

        RIGHT JOIN tabela2 on tabela1.coluna = tabela2.coluna;

    FULL JOING
        - Retorna todas as linhas de ambas as tabelas envolvidas na junção,
        combinando-as com base em um condição de igualdade. Se não houver
        correspondência, os valores ausentes serão preenchidos com NULL.

        SELECT *

        FROM tabela1

        FULL JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

    Sub Consultas
        - Elas permitem realizar consultas mais complexas permitindo
        que você use o resultado de uma consulta como entrada para
        outra consulta.

        As subconsultas podem ser usadas em várias partes de uma
        consulta:

        - SELECT
        - FROM
        - WHERE
        - HAVING
        - JOIN
"""