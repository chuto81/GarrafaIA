import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
from datetime import datetime

def run():
    #Cargue de información
    estructura = pd.read_csv('Input1_clientes_estructura.csv', sep=';')
    ventas = pd.read_csv('Input2_clientes_venta.csv', sep=';')
    respuesta = pd.read_csv('Input3_clientes_test.csv', sep=';')
    

    #Creación de una fila para un valor consecutivo en meses
    ventas['fecha_mes'] = (ventas['Año'] - 2019) * 12 + (ventas['Mes'] - 4)
    #print(ventas['fecha_mes'])

    #Union de base de datos
    final = pd.merge(ventas, estructura, on='Cliente', how='left')
    #print(final.head())
    print(final.info())

    print("El dataframe tiene una dimención de:", final.shape)

    #id de Cliente a str "para no tomarlo como un valor numerico"
    final['Cliente'] = final['Cliente'].map(str) + 'AA'
    #print(final)

    #Valores Unicos
    unicosC = {}
    unicosClen = {}
    dfu1 = final
    
    for col in dfu1:
        #print(len(dfu1[col].unique()))
        unicosC[col]=(dfu1[col].unique())
        unicosClen[col]=len(dfu1[col].unique())

    
    print('Las opcciónes por caracteristica o (feature) son:')

    #print(unicosC)
    #num_col = len(final.columns)
    #print(num_col)
    print(unicosClen)
    
    #Creación espacio para probabilidades
    proba = {}

    for col2 in unicosC:
        proba[col2] = (1/len(unicosC[col2]))

    #print(proba)

    newp = pd.DataFrame.from_dict([proba])
    print(newp*100)

    #Inputs del usuario:
    print('\n')
    print('¿En que mes se realiza la transacción?, Enero es 1 y Diciembre es 12')
    print('Ingresa el valor de ingreso esperado en este negocio unidad = moneda millones|ejemplo=8.4')
    print('¿Le vas a dar descuento? unidad = moneda millones, ejemplo 1.2')
    mes_user = int(input("Mes:"))+4
    revenue_user = float(input("Ingreso esperado"))
    descuento_user = float(input("Descuento"))
    
    
    
    

    print('\n')
    print('<<------------------------------Modelo------------------------------------>>')

   # x = disc - nr - fecha_mes
    x = final.iloc[:, 8:11].values

    # y = Volumen
    y = final.iloc[:, -9].values

    # reshape para 2D, no para 3D en adelante

    y = y.reshape(-1, 1)
    #x = x.reshape(-1, 1)
    x

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

    X_train[:,1]

    reg = LinearRegression()
    reg.fit(X_train, Y_train)
    #print(reg.fit(X_train, Y_train))
    print('El coeficiente es:', reg.score(X_test, Y_test)*100)

    print('<<------------------------------Predicción------------------------------------>>')
    X_objetivo = np.array([[descuento_user,  revenue_user, mes_user]])
    Y_pred = reg.predict(X_objetivo)
    print('El volumen predecido es: {}'.format(Y_pred))



#Variables
#1. medias
#Multi index Marca+mes+recuento de registros
    recmean_1 = 23913
    recmean_2 = 2625
    recmean_3 = 2353

#--------------------------
#suma
    rn_m1 = 59341177.3
    rn_m2 = 683983.3 
    rn_m3 = 1064539.8

#---------------------------  
#suma
    v_m1 = 8456.4
    v_m2 = 88.5
    v_m3 = 1.5
#--------------------------
#--------------------------Recuentos y sumas generales
    tr = final.groupby(['fecha_mes']).agg({'fecha_mes':['count']})
    print(tr)

    tnr = final.groupby(['fecha_mes']).agg({'nr':['sum']})
    print(tnr)

    tV = final.groupby(['fecha_mes']).agg({'Volumen':['sum']})
    print(tV)

#-------------------------------
    #recuento/total de los registros en el mes x marca
    p_marca1_cuenta = recmean_1/tr.mean()
    p_marca2_cuenta = recmean_2/tr.mean()
    p_marca3_cuenta = recmean_3/tr.mean()
    #Promedio de revenue x marca = suma de revenue neto / Total de revenue promedio en todos los meses xmarca
    p_marca1_nr = rn_m1/tnr.mean()
    p_marca2_nr = rn_m2/tnr.mean()
    p_marca3_nr = rn_m3/tnr.mean()
    #promedio de volumen x marca = suma de rvolumen / Volumen promedio en todos los meses x marca
    p_marca1_v = v_m1/tV.mean()
    p_marca2_v = v_m1/tV.mean()
    p_marca3_v = v_m3/tV.mean()
#-----------------------------------
    #3 escenarios de Probabilidades comparando con las otras 39 marcas
    print("probabilidades: ", p_marca1_cuenta , " ", p_marca2_cuenta, " ", p_marca3_cuenta)
    pmr = [p_marca1_cuenta, p_marca2_cuenta,  p_marca3_cuenta]
    suma3m = p_marca1_cuenta + p_marca2_cuenta + p_marca3_cuenta
    print("Probabilidad de que sea una de las 3 marcas por el recuento: ", suma3m )

    print("probabilidades: ", p_marca1_nr , " ", p_marca2_nr, " ", p_marca3_nr)
    suma3nr = p_marca1_nr + p_marca2_nr + p_marca3_nr
    print("Probabilidad de que sea una de las 3 marcas por el Revenue: ", suma3nr )

    print("probabilidades: ", p_marca1_v , " ", p_marca2_v, " ", p_marca3_v)
    suma3v = p_marca1_v + p_marca2_v + p_marca3_v
    print("Probabilidad de que sea una de las 3 marcas por el Volumen ", suma3v )


# Clasificación resta con respecto a las 3 marcas
    print(Y_pred[0][0])
    d1 =float(abs(Y_pred[0][0] - p_marca1_v))  
    d2 =float(abs(Y_pred[0][0] - p_marca2_v))
    d3 =float(abs(Y_pred[0][0] - p_marca3_v))

    print('probabilidad marca_1:', d1)
    print('probabilidad marca_2:', d2)
    print('probabilidad marca_3:', d3)
    
    dif= [d1,d2,d3]
    sdif=sum(dif)
    sdif=sum(dif)
    #Probabilidad segun la diferencia del erro con respecto al pronostico
    psdif = list(map(lambda x: x / sdif, dif))
    psdif

    #psdifT = list(map(lambda x: x, dif))

    mini_index = dif.index(min(dif))

    print('-----------------Probabilidad segun Recuento de registros + pronostico-----------------------------------')
    print("mejor ajuste a la marca_", mini_index+1, '|obtenida por diferencia con la media de la marca_',mini_index+1,'|: ', min(dif))
    
    print('-----------------Probabilidad segun Recuento de registros + pronostico-----------------------------------')
    
    
    print('Probalidad para la marcas 1,2,3', psdif)

    
    # Probabilidad de que sea una marca segun el volumen * Probabilidad segun el recuento
    res_list = [] 
    for i in range(len(psdif)): 
        res_list.append(psdif[i] * pmr[i] ) 

    s_res_list = sum(res_list)

    
    print('Probalidad para la marcas segun volumen. 1,2,3', psdif)
    print('-------------------------------------------------------------')
    print('Probalidad segun volumen * Probalidad segun recuento 1,2,3\n', res_list)
    print('\n')
    print('Probalidad 3 marcas\n', s_res_list)
 
    otras_marcas_p = (1-s_res_list)/38
    print('\n')
    print('Probalidad 3 marcas\n', otras_marcas_p)

    print('\n')
    print('\n')
    print('\n')

    print('P_marca_1:', res_list[0])
    print('P_marca_2:', res_list[1])
    print('P_marca_3:', res_list[2])
    print('P_marca_4:', otras_marcas_p)
    print('P_marca_5:', otras_marcas_p)

    print('\n')
    print('\n')
    print('\n')

    print('¿Quiere tener en cuenta otra variable?, alfrente del nombre de la variable digite (1)')
    v1 = int(input('SegmentoPrecio'))
    v2 = int(input('Cupo'))
    v3 = int(input('CapacidadEnvase'))
    v4 = int(input('CapacidadEnvase'))
    v5 = int(input('Categoria'))
    v6 = int(input('Nevera'))

    variables_a_considerar = [v1,v2,v3,v4,v5,v6]
    
    print(proba[1])

    #for v in variables_a_considerar:
    #    variables_a_considerar
    #print('\n')
if __name__ == "__main__":
    run()


