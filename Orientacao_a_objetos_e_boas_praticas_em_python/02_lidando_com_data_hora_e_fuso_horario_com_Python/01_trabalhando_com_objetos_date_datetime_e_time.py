"""
    O que é o módulo datetime?
        O módulo 'datetime' em Python é usado para lidar com datas e
        horas. Ele possuí várias classes úteis como date, time e timedelta.
"""

from datetime import date, datetime, time

d = date(2023, 7, 19)
print(d)

print(date.today())

data_hora = datetime(2023, 7, 10)
print(data_hora)
print(datetime.today())


hora = time(10, 20, 0)
print(hora)