"""
    Introdução

    Python também permite converter e formatar datas e horas.
    Para isso, usamos os métodos 'strftime' (string format time)
    e 'strptime' (string parse time).

    Exemplo

import datetime

d = datetime.datetime.now()

# formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M"))

# convertendo string para datetime
date_string = "20/07/2024 15:30"
d = datetime.datime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)

    Documentação

docs.python.org/pt-br/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior
"""

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2024-10-20 10:20'
mascara_ptbr = '%d/%m/%Y %A'
mascara_en = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(data_convertida.strftime('%Y'))
print(type(data_convertida))