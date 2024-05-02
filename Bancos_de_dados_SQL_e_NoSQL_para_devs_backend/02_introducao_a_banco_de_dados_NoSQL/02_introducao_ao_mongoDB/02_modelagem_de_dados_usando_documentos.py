"""
    Coleções
    - Agrupamento lógico de documentos
    - Não exige esquema ou que os documentos tenham a mesma estrutura

    Caractetísitcas
    - Os nomes das coleções devem seguir algumas regras:
        - Devem começar com uma letra ou um undescore ( _ )
        - Podem conter letras, números ou underscores
        - Não podem ser vazios
        - Não podem ter mais de 64bytes de comprimento
    
    Documentos
    - São armazenados em documentos BSON (Binary JSON), que são
    estruturas flexíveis e semiestruturadas
    - Cada documento possui um identificador único chamado "_id"
    - É composto por pares de chaves e valores
    - Tamanho máximo: Cada documento no MongoDB pode ter um tamanho máximo
    de 16 MB
    - Aninhamento de documentos
    - Flexibilidade na evolução do esquema

    Tipos de dados simples
    - String
    - Number
    - Boolean
    - Date
    - Null
    - ObjectId

    Tipos de dados complexos
    - Array
    - Documento Embutido (embedded Document)
    - Referência (reference)
    - GeoJSON

    Estrutura de um documento
        {
            _id: ObjectId(""),
            "nome_campo":"valor_campo",
            ...
        }

    Modelagem da estrutura do Usuário e Destinos
        https://jsonformatter.curiousconcept.com/

    Links Úteis
    - https://www.mongodb.com/docs/manual/reference/bson-types/

    - https://www.mongodb.com/docs/manual/reference/geojson#std-label-geojson-point
"""