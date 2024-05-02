"""
    Funções Agregadas
    - COUNT: Conta o número de registros
    - SUM: Soma os valores de uma coluna numérica
    - AVG: Calcula a média dos valores de uma coluna numérica
    - MIN: Retorna o valor mínimo de uma coluna.
    - MAX: Retorna o valor máximo de uma coluna.

    Exemplos:
        SELECT COUNT(*) as total_usuarios FROM usuarios us;

        SELECT COUNT(*) as total_usuarios FROM usuarios us
        INNER JOIN reservas rs ON us.id = rs.id_usuario;

        SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATA()))
        as maior_idade FROM usuarios us;

    
    Agrupamento de Resultados
        - SELECT
        - FROM
        - GROUP BY

    Exemplos:
        SELECT COUNT(*) AS qtd_reservas, id destino FROM reservas
        GROUP BY id_destino
        ORDER BY qtd_reservas;
    
"""