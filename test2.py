import pandas as pd
import re



url = ['https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv',
	'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/CasosTotalesCumulativo.csv',
	'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto19/CasosActivosPorComuna.csv']
df_totales_comuna = pd.read_csv(url[0],sep=',')
df_totales_region = pd.read_csv(url[1],sep=',') 
df_totales_activos_region_comuna = pd.read_csv(url[2],sep=',') 


df_region = df_totales_activos_region_comuna[df_totales_activos_region_comuna['Comuna'] == 'Total']
#print(df_totales_comuna['Comuna'])
a,b = 'áéíóúü','aeiouu'
trans  = str.maketrans(a,b)

regiones_name = []
print(df_totales_comuna['Region'])
df_biobio = df_totales_comuna[df_totales_comuna['Region']== 'Biobío']
print(df_biobio)
for region in df_totales_comuna['Region']:
	
	region2 = region.translate(trans)
	df_totales_comuna['Region'] = df_totales_comuna['Region'].replace([region],[region2])
	#region2 = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", '',region)
print(df_totales_comuna['Region'])
df_biobio2 = df_totales_comuna[df_totales_comuna['Region']== 'Biobio']
print(df_biobio2)
#print(df_region['Region'])

