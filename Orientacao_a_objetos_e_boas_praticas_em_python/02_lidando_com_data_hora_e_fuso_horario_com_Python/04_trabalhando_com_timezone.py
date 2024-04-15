"""
    Introdução

    Quando trabalhamos com data e hora, lidas com fusos horários
    é uma necessidade comum. Python facilita isso através do módulo
    'pytz'.

    Exemplo

# pip install pytz

import datetime
import pytz

# Criando datetime com timezone
d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo))
print(d)
    

en.wikipedia.org/wiki/List_of_tz_database_time_zones
"""

import datetime
import pytz

# Criando datetime com timezone
d = datetime.datetime.now(pytz.timezone("America/Cuiaba"))
print(d)


"""
    Trabalhando com tz sem bibliotecas externas

    O Python permite fazer isso com o módulo datetime padrão,
    embora seja um pouco mais complexo do que usando bibliotecas
    como 'pytz'.

"""

from datetime import datetime, timezone, timedelta

# Criando datetime com timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_ms = datetime.now(timezone(timedelta(hours=-4)))

print(data_oslo)
print(data_ms)