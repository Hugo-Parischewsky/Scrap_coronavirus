import os
import time
from datetime import datetime
import pandas as pd

def comuna(nombre,df,df_activos):
	'''
	esta funcion retorna el valor de los casos activos totales/ultimo dia/activo
	los datos que extrae son del repositorio 
	esto itera sobre los nombres de las ciudades
	name: nombre ciudad para conocer casos totales activods y del ultimo dia [str]
	'''
	try:
		df_ciudad_ingresada = df[df['Comuna']==str(nombre)]
		fecha_last = df_ciudad_ingresada.columns[-2]
		fecha_pre_last = df_ciudad_ingresada.columns[-3]
		totales_last = df_ciudad_ingresada[fecha_last].values[0]
		totales_pre_last = df_ciudad_ingresada[fecha_pre_last].values[0]
		region = df_ciudad_ingresada.columns[0]
		region_nombre = df_ciudad_ingresada[region].values[0]
		totales_ultimo_dia = totales_last - totales_pre_last

		df_activos_comuna = df_3[df_3['Comuna'] == str(nombre)]
		fecha_3 = df_activos_comuna.columns[-1]
		activos = df_activos_comuna[str(fecha_3)].values[0]


		return totales_last,region_nombre,fecha_last,totales_ultimo_dia,activos,fecha_3
	except:
		print('Nombre ingresado no valido')
		return False

def region(nombre,df,df_activos):
	'''
	esta funcion retorna el valor de los casos activos totales/ultimo dia/activo
	los datos que extrae son del repositorio 
	esto itera sobre el nombre de las regiones.
	name: nombre ciudad para conocer casos totales activods y del ultimo dia [str]
	'''
	try:
		df_region_ingresada = df[df['Region']==str(nombre)]
		fecha_last = df_region_ingresada.columns[-1]
		totales_last = df_region_ingresada[str(fecha_last)].values[0]

		fecha_pre_last = df_region_ingresada.columns[-2]
		totales_pre_last = df_region_ingresada[str(fecha_pre_last)].values[0]

		totales_ultimo_dia = totales_last - totales_pre_last

		df_region_ingresada_activos = df_activos[df_activos['Region'] == str(nombre)]
		activos = df_region_ingresada_activos[str(fecha_last[0])]



		return totales_last,fecha_last,totales_ultimo_dia,activos
	except:
		print('Nombre ingresado no valido')
		return False

url = ['https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv',
		'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/CasosTotalesCumulativo.csv',
		'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto19/CasosActivosPorComuna.csv']
df_1 = pd.read_csv(url[0],sep=',')
df_2 = pd.read_csv(url[1],sep=',') 
df_3 = pd.read_csv(url[2],sep=',') 


### pasar a una funcion 
if os.path.isfile('./comunas_list.txt') == True:
	print('existe el directorio comuna')
	x = open('./comunas_list.txt','r+')
	for comuna_ in df_1['Comuna'].values:
	    x.write(str(comuna_)+'\n')
	x.close()
else:
	print('no existe el directorio comuna')
	x = open('./comunas_list.txt','w')
	x.close()
	print('directorio creado')
	x = open('./comunas_list.txt','r+')
	for comuna_ in df_1['Comuna'].values:
	    x.write(str(comuna_)+'\n')
	x.close()
### pasar a una funcion
if os.path.isfile('./regiones_list.txt') == True:
	print('existe el directorio region')
	xx = open('./regiones_list.txt','r+')
	for region_ in df_1['Region'].values:
	    xx.write(str(region_)+'\n')
	xx.close()
else:
	print('no existe el directorio region')
	xx = open('./regiones_list.txt','w')
	xx.close()
	print('directorio creado')
	xx = open('./regiones_list.txt','r+')
	for region_ in df_1['Region'].values:
	    xx.write(str(region_)+'\n')
	xx.close()




### menu options and define

menu = {}
menu['1']="Ingrese nombre de region." 
menu['2']="Ingrese nombre de comuna."
menu['3']="Abrir lista nombres comuna"
menu['4']="Abrir lista nombres regiones"
menu['5']="Salir \n"
while True: 
	print(' 			Datos cargados del repositorio del MINSAL .')
	print('')
	options=menu.keys()
	options = sorted(options)
	#options.sort()
	for entry in options: 
		print(entry, menu[entry])

	selection=input("Seleccione opcion : ") 
	if selection =='1': 	
		palabra_region = input('Ingrese el nombre de la region: ')
		region_funcion = region(palabra_region,df_2,df_3)
		valor,fecha,last_day,activos = region_funcion[0],region_funcion[1],region_funcion[2],region_funcion[3]
		palabra_comuna = ''

		### pasar a una funcion
		os.system('clear')
		now = datetime.now()
		current_time = str(now.strftime("%H:%M:%S"))
		print('''
Region: {}
Comuna: {}
Casos totales: {}	-> {} <- Last Upload
Casos activos: {}	-> {} <- Last Upload
Casos Ultimo dia: {}

		'''.format(palabra_region,palabra_comuna,valor,fecha,activos,fecha_activos,last_day))
		print('\n \nLast update: ', current_time)
				
		time.sleep(0.1)
	elif selection == '2': 
		palabra_comuna = input('Ingrese el nombre de la comuna: ')
		comuna_funcion = comuna(palabra_comuna,df_1,df_3)
		valor,palabra_region,fecha,last_day,activos,fecha_activos  = comuna_funcion[0],comuna_funcion[1],comuna_funcion[2],comuna_funcion[3],comuna_funcion[4],comuna_funcion[5]
		
		### Pasar a una funcion
		os.system('clear')
		now = datetime.now()
		current_time = str(now.strftime("%H:%M:%S"))
		print('''
Region: {}
Comuna: {}
Casos totales: {}	-> {} <- Last Upload
Casos activos: {}	-> {} <- Last Upload
Casos Ultimo dia: {}

		'''.format(palabra_region,palabra_comuna,valor,fecha,activos,fecha_activos,last_day))
		print('\n \nLast update: ', current_time)
				
		time.sleep(0.1)
	elif selection == '3':
		os.system('open comunas_list.txt')
		os.system('clear')
	elif selection == '4':
		os.system('open regiones_list.txt')
		os.system('clear')
	elif selection == '5': 
		break
	else: 
		os.system('clear')
		print('Numero ingresado no valido')


	
