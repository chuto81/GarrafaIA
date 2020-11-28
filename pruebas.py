from datetime import datetime
# Convertimos un string con formato <día>/<mes>/<año> en datetime
una_fecha = '20/04/2019'
fecha_dt = datetime.strptime(una_fecha, '%d/%m/%Y')
fecha_str = datetime.strftime(fecha_dt, '%d/%m/%Y')

print(fecha_dt)
print(fecha_str)
# 2019-04-20 00:00:00
# Comprobación del tipo del objeto fecha_dt
print(type(fecha_dt))
print(type(fecha_str))
#<class 'datetime.datetime'>