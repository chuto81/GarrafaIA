import pandas as pd
import numpy as np

#Cargue de información
estructura = pd.read_csv('Input1_clientes_estructura.csv', sep=';')
ventas = pd.read_csv('Input2_clientes_venta.csv', sep=';')
respuesta = pd.read_csv('Input3_clientes_test.csv', sep=';')

#Creación de una fila para un valor consecutivo en meses
ventas['fecha_mes'] = (ventas['Año'] - 2019) * 12 + (ventas['Mes'] - 4)

#Union de base de datos
final = pd.merge(ventas, estructura, on='Cliente', how='left')

#id de Cliente a str "para no tomarlo como un valor numerico"
#final['Cliente'] = final['Cliente'].map(str) + 'AA'

gp = final.groupby(['Cliente']).agg({'nr':'mean', 'disc':'mean'})

print(type(gp))

gp.to_csv(r'C:\Users\chuto\Dropbox\DESARROLLADOR\014_Hackaton Brewing 2020\Code\Input3_clientes_testPRUEBA.csv')
