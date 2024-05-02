"""
    Chave Primária
     - Identifica exclusivamente.
     - Não pode conter valores nulos (NULL).
     - Uma tabela pode ter apenas uma chave primária.

    CREATE TABLE  {{tabela}}
    (ID PRIMARY KEY AUTOINCREMENT,
    ...,);
    ALTER TABLE {{tabela}}
    MODIFY COLLUMN ID INT PRIMARY KEY;

    Chave Estrangeira
    - Ela é usada para estabelecer e manter a integridade dos
    dados entre tabelas relacionadas.

    - Pode ser nula (NOT NULL); **Registro Orfão
    - É possível ter mais de uma (ou nenhuma) em uma tabela.

    CREATE TABLE {{tabela}}(
        id INT PRIMARY KEY,
        chave_estrangeira INT,
       
        FOREIGN KEY (chave_estrangeira)
        REFERENCES {{outra_tabela}}(id)
    );

    ALTER TABLE {{tabela}}
    ADD CONSTRANT {{nome_constraint}}
    FOREING KEY (ID_)
    REFERENCES {{outra_tabela}} (ID)

    Chave Estrangeira - Restrições
    - ON DELETE especifica o que acontece com os registros
    dependentes quando um registro pai é excluído.
    - ON UPDATE define o comportamento dos registros
    dependnetes quando um registro pai é atualizado.
    - CASCADE, SET NULL, SET DEFAULT e RESTRICT
"""