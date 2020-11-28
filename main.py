import numpy as np
import pandas as pd

ventas = pd.read_csv(r'C:\Users\chuto\Dropbox\DESARROLLADOR\014_Hackaton Brewing 2020\Code\reto-colombia-2020\data\Input2_clientes_venta.csv', sep=';')
clientes = pd.read_csv(r'C:\Users\chuto\Dropbox\DESARROLLADOR\014_Hackaton Brewing 2020\Code\reto-colombia-2020\data\Input1_clientes_estructura.csv', sep=';')

print(type(ventas))
print(ventas.shape)

print(type(clientes))
print(clientes.shape)

