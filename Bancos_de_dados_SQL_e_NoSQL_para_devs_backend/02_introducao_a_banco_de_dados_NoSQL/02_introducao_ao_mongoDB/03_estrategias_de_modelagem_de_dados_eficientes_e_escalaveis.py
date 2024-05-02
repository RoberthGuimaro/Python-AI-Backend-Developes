"""'
    Modelagem orientada por consultas
    - A modelagem de dados no MongoDB deve ser orientada pelas consultas
    que serão realizadas com mais frequência.

    Inner Documents
    - No MongoDB, é comum denormalizar os dados para evitar operações
    de junção (join) custosa. Isso significa que os dados relacionados
    podem ser armazenados juntos em um único documento, em vez de serem
    distribuídos em várias coleções.

    Modelar usuário com estrategia desnormalizada
        https://jsonformatter.curiousconcept.com/

    Quando usar
    - Os dados aninhados são específicos para o documento pai
    - Os dados aninhados são sempre acessados juntamento com o documento pai
    - A cardinalidade do relacionamento é um-para-muitos (um usuário pode ter
    várias reservas).

    Quando não utilizar
    - Se os dados aninhados precisarem ser consultados e atualizados
    independente do documento pai, é mais adequado utilizar coleções separadas.


    Modelar usuário com estratégia de referência

    Referências
    - Forma de relacionar os documentos entre si.

    Quando usar
    - Os dados têm seu próprio significado e podem ser acessados 
    independentemente do documento pai.
    - Os dados têm uma cardinalidade mais alta (por exemplo, vários usuários
    podem ter reservas).

    Quando não usar
    - Se os dados aninhados não precisam ser consultados e atualizados
    independentemente do documento pai, é mais adequado utilizar coleçoes
    separadas.

    Links Úteis
    - https://www.luiztools.com.br/post/padroes-para-modelage-de-dados-documentos-em-mongodb/
"""