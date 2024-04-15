"""
    Introdução

    Podemos criar e manipular objetos date, time e datetime de
    varias maneiras. Por exemplo, podemos adicionar e subtrair
    datas, verificar a diferença entre dastas e muito mais.

    # Exemplo

import datetime

# Criando data e hora
d = datetime.datetime(2024, 4, 13, 17, 30)
print(d)

# Adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d)

# Documentação
# docs.python.org/pt-br/3/libray/datetime.html?highlight=datetime#timedelta-objects

"""

from datetime import date, time, datetime, timedelta

tipo_carro = 'P' # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto ás {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou: {data_atual} e ficará pronto ás {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou: {data_atual} e ficará pronto ás {data_estimada}')

print(date.today() - timedelta(days=1))

# Não é possível trabalhar apenas com o time é necessário o objeto completo
# a manipulação do objeto deve ser feito depois.
resultado = datetime(2024, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())