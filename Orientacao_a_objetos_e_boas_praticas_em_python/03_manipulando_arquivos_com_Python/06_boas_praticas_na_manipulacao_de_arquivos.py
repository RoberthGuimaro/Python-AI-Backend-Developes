"""
    Boas praticas na manipulação de arquivos

    - Ao manipular arquivos em Python existem algumas boas práticas
    que podemos seguir, vamos abordar as principais.

    Bloco with
    - Use o gerenciamento de contexto (context manager) com a
    declaração 'with'. O gerenciamento de contexto permite trabalhar
    com arquivos de forma segura, garantindo que eles sejam fechados
    corretamente, mesmo em caso de exceções.

    Verifique se o arquivo foi aberto com sucesso
    - É recomendado verificar se o arquivo foi aberto corretamente
    antes de executar operações de leitura ou gravação nele.

    Use a codificação correta
    - Certifique-se de usar a codificação correta ao ler ou gravar
    arquivos de texto. O argumento 'encoding' da função 'open()'
    permite especificar a codificação.
    
"""

from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'lorem.txt', 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())

except FileNotFoundError as exc:
    print(f"Arquivo não existente {exc}")

except IOError as exc:
    print(f"Erro ao abrir o arquivo, {exc}")


try:
    with open(ROOT_PATH / 'arquivo-utf-8.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Aprendendo a manipular arquivos utilizando Python.')

except IOError as exc:
    print(f'Erro ao abrir o arquivo {exc}')