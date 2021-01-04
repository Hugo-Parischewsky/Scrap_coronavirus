import pandas as pd
import re

def region(nombre,df,df_activos):
	'''
	esta funcion retorna el valor de los casos activos totales/ultimo dia/activo
	los datos que extrae son del repositorio 
	esto itera sobre el nombre de las regiones.
	name: nombre ciudad para conocer casos totales activods y del ultimo dia [str]
	'''
	df_region_ingresada = df[df['Region']==str(nombre)]
	fecha_last = df_region_ingresada.columns[-1]
	totales_last = df_region_ingresada[str(fecha_last)].values[0]

	fecha_pre_last = df_region_ingresada.columns[-2]
	totales_pre_last = df_region_ingresada[str(fecha_pre_last)].values[0]

	totales_ultimo_dia = totales_last - totales_pre_last


	df_region_ingresada_activos = df_activos[df_activos['Region'] == str(nombre)]
	fecha_last_activos = df_region_ingresada_activos.columns[-1]
	activos = df_region_ingresada_activos[str(fecha_last_activos[0])].values[0]



	return totales_last,fecha_last,totales_ultimo_dia,activos

url = ['https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv',
	'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/CasosTotalesCumulativo.csv',
	'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto19/CasosActivosPorComuna.csv']
df_1 = pd.read_csv(url[0],sep=',')
df_2 = pd.read_csv(url[1],sep=',') 
df_3 = pd.read_csv(url[2],sep=',') 




#palabra_region = input('Ingrese el nombre de la region: ')
palabra_region1 = 'Biobío'
palabra_region2 = 'Biobio'
#print(df_2['Region'])
#region_funcion = region(palabra_region,df_2,df_3)
df_region_ingresada = df_2[df_2['Region']==str(palabra_region1)]
#print(df_region_ingresada)
fecha_last = df_region_ingresada.columns[-1]
#print(fecha_last)
totales_last = df_region_ingresada[str(fecha_last)].values[0]
#print(totales_last)

fecha_pre_last = df_region_ingresada.columns[-2]
#print(fecha_pre_last)
totales_pre_last = df_region_ingresada[str(fecha_pre_last)].values[0]
#print(totales_pre_last)
totales_ultimo_dia = totales_last - totales_pre_last
#print(totales_ultimo_dia)

###
df_region = df_3[df_3['Comuna'] == 'Total']
df_region_ingresada_activos = df_region[df_region['Region'] == str(palabra_region2)]
#print(df_region_ingresada_activos)
fecha_last_activos = df_region_ingresada_activos.columns[-1]

activos = df_region_ingresada_activos[str(fecha_last_activos)].values[0]
print(fecha_last_activos)
