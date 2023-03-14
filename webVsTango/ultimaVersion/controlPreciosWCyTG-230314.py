#########################################################################################################
#LIBRERIAS
#########################################################################################################
import pandas as pd #OK
import numpy as np 	#OK
import datetime as dt
import logging 
import os
import pathlib
import glob
import pyodbc as po 	#DESCARGA: https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15


#########################################################################################################
#DEFINICIONES
#########################################################################################################


#########################################################################################################
def logErrores(ruta,):
#########################################################################################################
	global logger

	log=ruta+f'{dt.datetime.now().strftime("%Y-%m-%d")}.txt'
	print(f'Log cargado en: {log}')
	check=os.makedirs(os.path.dirname(log),exist_ok=True)
	logging.basicConfig(filename=log, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - at line: %(lineno)d - %(message)s')
	logger=logging.getLogger('logErrores')

#########################################################################################################
def plog(notas):
#########################################################################################################
	print(dt.datetime.now().strftime('%m-%d %H:%M:%S:%f'),"- "+str(notas))
	logger.debug(str(notas))



#########################################################################################################
def conexSql(server,database,username,password,query):
#########################################################################################################
	global consulta
	global cabecerasSql
	global filasSql

	cnxn=po.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+';TrustServerCertificate=YES')
	consulta=cnxn.cursor().execute(query)   
	cabecerasSql=[i[0] for i in consulta.description]
	filasSql=consulta.fetchall()
	cnxn.commit()



################################################################################################################################
def main():
################################################################################################################################

	#BUSCA PRODUCTOS WC
	hoy=dt.datetime.now().strftime('%d-%m-%Y') # %H:%M:%S:%
	hoy=hoy.lstrip("0").replace(" 0", " ") #Quita cero de dia
	hoy=hoy.lstrip("0").replace("-0", "-") #Quita cero de mes
	plog(hoy)
	extWeb=r"C:\Users\gpereyra\Downloads\wc-product-export-"+hoy+r"*.csv"
	#extWeb=r"**\wc-product-export-"+hoy+r"*.csv"
	#print(list(glob.glob(extWeb))[0])
	origenWeb=list(glob.glob(extWeb))[0]
	#origenWeb=list(pathlib.Path().glob(extWeb))[0]
	plog("Origen de datos web a trabajar: "+str(origenWeb))


################################################################################################################################
	#BUSCA PRODUCTOS TANGO
	server='HCSANMARTIN.DDNS.NET,5001'  #'IRONSERVER\\HIERROS1' #'ironserver,1183' #localhost,1183  #puerto 1183 #ironserver.hcllavallol2001.dbo.gva17
	database='HCSANMARTIN'  #'hcllavallol2001' 
	username='Axoft' #'testuser' 
	password='Axoft' #'usertest' 
	query="""
	SELECT G.[COD_ARTICU],CAST(G.[PRECIO] AS DECIMAL(20,2)) [PRECIO], CAST(G.[PRECIO]*S.[EQUIVALE_V] AS DECIMAL(20,2)) [PRECIO-U], G.[FECHA_MODI], S.[PERFIL] --[ID_GVA17],[BASE],[FECHA_PRECIOS_PEDIDOS],[FILLER],[NRO_DE_LIS], --[ID_GVA17],[BASE],[FECHA_PRECIOS_PEDIDOS],[FILLER],[NRO_DE_LIS],
	FROM [{}].[dbo].[GVA17] G
	INNER JOIN [{}].[dbo].[STA11] S
	ON G.COD_ARTICU=S.COD_ARTICU
	WHERE (G.COD_ARTICU LIKE '00010%'
	OR G.COD_ARTICU LIKE '00020%'
	OR G.COD_ARTICU LIKE '00030%'
	OR G.COD_ARTICU LIKE '00050%'
	OR G.COD_ARTICU LIKE '00060%'
	OR G.COD_ARTICU LIKE '00070%'
	OR G.COD_ARTICU LIKE '00120%'
	OR G.COD_ARTICU LIKE '00130%'
	OR G.COD_ARTICU LIKE '00140%'
	OR G.COD_ARTICU LIKE '00150%'
	OR G.COD_ARTICU LIKE '00160%'
	OR G.COD_ARTICU LIKE '00170%'
	OR G.COD_ARTICU LIKE '00250%'
	OR G.COD_ARTICU LIKE '00370%'
	OR G.COD_ARTICU LIKE '00510%'
	OR G.COD_ARTICU LIKE '00560%'
	OR G.COD_ARTICU LIKE '00610%'
	OR G.COD_ARTICU LIKE '01250%'
	OR G.COD_ARTICU LIKE '01330%'
	OR G.COD_ARTICU LIKE '01340%'
	OR G.COD_ARTICU LIKE '01930%'
	OR G.COD_ARTICU LIKE '02150%'
	OR G.COD_ARTICU LIKE '02160%'
	OR G.COD_ARTICU LIKE '02370%'
	OR G.COD_ARTICU LIKE '02450%'
	OR G.COD_ARTICU LIKE '03180%'
	OR G.COD_ARTICU LIKE '03260%'
	OR G.COD_ARTICU LIKE '03270%'
	OR G.COD_ARTICU LIKE '03280%'
	OR G.COD_ARTICU LIKE '03290%'
	OR G.COD_ARTICU LIKE '03300%'
	OR G.COD_ARTICU LIKE '03320%'
	OR G.COD_ARTICU LIKE '03390%'
	OR G.COD_ARTICU LIKE '03530%'
	OR G.COD_ARTICU LIKE '03540%'
	OR G.COD_ARTICU LIKE '03550%'
	OR G.COD_ARTICU LIKE '04100%'
	OR G.COD_ARTICU LIKE '04120%'
	OR G.COD_ARTICU LIKE '04190%'
	OR G.COD_ARTICU LIKE '04320%'
	OR G.COD_ARTICU LIKE '06820%'
	OR G.COD_ARTICU LIKE '06830%'
	OR G.COD_ARTICU LIKE '06840%'
	OR G.COD_ARTICU LIKE '06850%'
	OR G.COD_ARTICU LIKE '06900%'
	OR G.COD_ARTICU LIKE '07240%'
	OR G.COD_ARTICU LIKE '08000%'
	OR G.COD_ARTICU LIKE '10020%'
	OR G.COD_ARTICU LIKE '10030%'
	OR G.COD_ARTICU LIKE '10040%'
	OR G.COD_ARTICU LIKE '10050%'
	OR G.COD_ARTICU LIKE '10060%'
	OR G.COD_ARTICU LIKE '10070%'
	OR G.COD_ARTICU LIKE '10080%'
	OR G.COD_ARTICU LIKE '10090%'
	OR G.COD_ARTICU LIKE '010000%'
	OR G.COD_ARTICU LIKE '010200%'
	OR G.COD_ARTICU LIKE '010700%'
	OR G.COD_ARTICU LIKE '010800%'
	OR G.COD_ARTICU LIKE '012000%'
	OR G.COD_ARTICU LIKE '012100%'
	OR G.COD_ARTICU LIKE '012200%'
	OR G.COD_ARTICU LIKE '023300%'
	OR G.COD_ARTICU LIKE '023400%'
	OR G.COD_ARTICU LIKE '023500%'
	OR G.COD_ARTICU LIKE '023600%'
	OR G.COD_ARTICU LIKE '087000%'
	OR G.COD_ARTICU LIKE '090900%'
	OR G.COD_ARTICU LIKE '091000%'
	OR G.COD_ARTICU LIKE '091100%'
	OR G.COD_ARTICU LIKE '092000%'
	OR G.COD_ARTICU LIKE '093000%'
	OR G.COD_ARTICU LIKE '094000%'
	OR G.COD_ARTICU LIKE '095000%'
	OR G.COD_ARTICU LIKE '096000%'
	OR G.COD_ARTICU LIKE '097000%'
	OR G.COD_ARTICU LIKE '098000%'
	OR G.COD_ARTICU LIKE '099000%'
	OR G.COD_ARTICU LIKE '001100%'
	OR G.COD_ARTICU IN ('023600000000020','023300000000050','019600000000030','019600000000010','023300000000050','023600000000010','023600000000050','019600000000040','001000000000010','001000000000020','001000000000030','072100000000010','072100000000020','072100000000030','072200000000010','072200000000020','072200000000030','072300000000010','072300000000020','072300000000030','011500000000060','011500000000070','011500000000110'))
	AND G.COD_ARTICU NOT IN ('001700000001255','093000000000270','000100000000080','000100000000682','000200000000010','000200000000180','000200000000280','000300000000010','000300000000620','000300000000630','000300000000640','000300000000670','000300000000760','000300000000770','000300000000780','000300000000960','000300000001120','000500000000180','000700000000130','000700000000170','001500000000090','001500000000140','01500000000150','001500000000210','001500000000260','001500000000470','001500000000530','001500000000991','001500000001080','001500000001085','001500000001090','001500000001100','001500000001104','001500000001105','001500000001106','001500000001107','001500000001108','001500000001109','001500000001110','001500000001120','001500000001130','001500000001131','001500000001140','001500000001147','001500000001150','001600000000395','001600000000452','001600000000650','001600000000660','001600000000662','001700000000364','001700000000395','001700000000400','001700000000410','001700000000420','001700000000440','001700000000565','001700000000655','001700000000800','001700000001160','001700000001280','001700000001300','001700000001310','001700000001320','001700000001323','003700000000010','003700000000020','003700000000030','003700000000061','005100000000020','005100000000030','005100000000040','005100000000100','012500000000015','012500000000104','012500000000122','012500000000123','019300000000010','019300000000100','019300000000110','019300000000120','019300000000130','019300000000140','019300000000190','019300000000230','023700000000080','023700000000126','023700000000205','023700000000230','023700000000270','023700000000280','023700000000320','023700000000331','023700000000345','031800000000045','031800000000220','032600000000015','032600000000030','033000000000140','033000000000150','033000000000160','033200000000070','033200000000080','035300000000010','035300000000020','035300000000030','041900000000002','041900000000273','043200000000050','012200000000040','023300000000060','023500000000040','023500000000050','023600000000110','023600000000120','032900000000065','041900000000090','068300000000020','068300000000030','068300000000040','019300000000240','080000000000120','010700000000010','010700000000020','010800000000010','010800000000020','010800000000030','010800000000040','010800000000050','012000000000070','012000000000071','012000000000080','012000000000090','012000000000100','012100000000010','012100000000030','012100000000040','012100000000050','012100000000060','012100000000070','012200000000010','012200000000015','012200000000020','012200000000030','012200000000050','012200000000060','012200000000070','019600000000010','019600000000030','019600000000040')
	AND S.PERFIL IN ('A','V','C')
	AND G.NRO_DE_LIS='1'
	ORDER BY G.[COD_ARTICU] ASC
	""".format(database,database)

	conexSql(server,database,username,password,query)
	cabeceras1=[cabecerasSql]    #Cabecera de consulta extraida de SQL.
	filas1=[filasSql]            #Filas de consulta extraida de SQL.
	con=0
	consultaTango=[]
	#print(len(cabeceras1[0]))
	consultaTango.append([str(con)])
	#METE RESULTADO DE CONSULTA SQL EN LISTA PYTHON
	print("Consulta TANGO:")
	print("###########################################################################################################")
	for i in range(0,len(cabeceras1[0])): 
	      consultaTango[0].append(cabeceras1[0][i])
	for i in range(0,len(filas1[0])):         # for i in range(0,len(cabeceras1[0])): print(str(cabeceras1[0][i])      
	      con+=1
	      consultaTango.append([con,filas1[0][i][0],round(filas1[0][i][1],2),filas1[0][i][2]])      
	plog(str("SQL: "+str(len(consultaTango))))

	# for i in range(1,len(consultaTango)):
	# 	print(consultaTango[i][0],consultaTango[i][1],float(consultaTango[i][2]),float(consultaTango[i][3]))

	################################################################################################################################

	


	#LEE PRODUCTOS DE WC

	datosWebCsv=pd.read_csv(origenWeb,header=0)
	pd.options.display.float_format = '{:.2f}'.format
	pd.set_option('display.max_rows', None)
	#print("datosWebCsv:")
	plog(str("CSV: "+str(len(datosWebCsv))))
	# print(datosWebCsv)

	# for i in range(1,len(datosWebCsv)):
	# 	print(datosWebCsv['SKU'],datosWebCsv['Publicado'],datosWebCsv['Precio normal'])

	
	fam=['010000','001000','010700','010800','010200','010700','010800','011500','012000','012100','012200','023300','023400','023500','023600','090900','091000','091100','092000','093000','094000','095000','096000','097000','098000','099000','072100','072200','072300']
	datosWebSoloU=[]

	#CONDICION DE PANDAS PARA TOMAR LAS FAMILIAS QUE SON VENTA SOLO POR UNIDADES:
	datosWebSoloU=datosWebCsv[datosWebCsv['SKU'].str.startswith('010000') | datosWebCsv['SKU'].str.startswith('010200') | datosWebCsv['SKU'].str.startswith('010700') | datosWebCsv['SKU'].str.startswith('010800') | datosWebCsv['SKU'].str.startswith('011500') | datosWebCsv['SKU'].str.startswith('012000') | datosWebCsv['SKU'].str.startswith('012100') | datosWebCsv['SKU'].str.startswith('012200')  | datosWebCsv['SKU'].str.startswith('023300')  | datosWebCsv['SKU'].str.startswith('023400') | datosWebCsv['SKU'].str.startswith('023500') | datosWebCsv['SKU'].str.startswith('023600') | datosWebCsv['SKU'].str.startswith('090900') | datosWebCsv['SKU'].str.startswith('091000') | datosWebCsv['SKU'].str.startswith('091100') | datosWebCsv['SKU'].str.startswith('092000') | datosWebCsv['SKU'].str.startswith('093000') | datosWebCsv['SKU'].str.startswith('094000') | datosWebCsv['SKU'].str.startswith('095000') | datosWebCsv['SKU'].str.startswith('096000') | datosWebCsv['SKU'].str.startswith('097000') | datosWebCsv['SKU'].str.startswith('098000') | datosWebCsv['SKU'].str.startswith('099000') | datosWebCsv['SKU'].str.startswith('10040') | datosWebCsv['SKU'].str.startswith('10050') | datosWebCsv['SKU'].str.startswith('10060') | datosWebCsv['SKU'].str.startswith('10070') | datosWebCsv['SKU'].str.startswith('10080') | datosWebCsv['SKU'].str.startswith('10090') | datosWebCsv['SKU'].str.startswith('072100') | datosWebCsv['SKU'].str.startswith('072200') | datosWebCsv['SKU'].str.startswith('072300') | datosWebCsv['SKU'].str.startswith('001000') | datosWebCsv['SKU'].str.startswith('019600') | datosWebCsv['SKU'].str.startswith('023600') | datosWebCsv['SKU'].str.startswith('023300')]
	# datosWebSoloU.remove('SKU')
	plog(str("SoloU: "+str(len(datosWebSoloU))))
	# pd.options.display.float_format = '{:.2f}'.format
	# pd.set_option('display.max_rows', None)
	# print(datosWebSoloU)



	#QUITA "-U" DE LOS PRODUCTOS POR UNIDAD 
	pd.set_option('mode.chained_assignment',None) #Elimina notificacion erronea.
	#datosWebSoloU['SKU']=datosWebSoloU['SKU'].str.slice(0,15)
	datosWebSoloU.loc[:,('SKU')]=datosWebSoloU.loc[:,('SKU')].str.slice(0,15)
	#print("datosWebSoloU")
	plog(str("SoloU sin -U: "+str(len(datosWebSoloU))))
	# pd.options.display.float_format = '{:.2f}'.format
	# pd.set_option('display.max_rows', None)
	# print(datosWebSoloU)

	
	#ELIMINA LOS PRODUCTOS POR UNIDAD (SOLO SE QUEDA CON LOS SKU POR KG)
	datosWebLimpios=datosWebCsv[~datosWebCsv['SKU'].str.endswith('-U')]		
	#print(datosWebLimpios)

	plog(str("Solo KG sin duplicados: "+str(len(datosWebLimpios))))
	# print(datosWebLimpios)

	
	#AGREGAR A LOS PRODUCTOS KG LOS PRODUCTOS POR UNIDAD PERO SIN EL SUFIJO "-U"
	datosWebLimpios=pd.concat([datosWebLimpios, datosWebSoloU]) #UNE DF DE KG CON DF DE -U
	#print("DWL y soloU: ",datosWebLimpios)

	plog(str("Todos: "+str(len(datosWebLimpios))))
	#print(datosWebLimpios)


	#FILTRA PRODUCTOS QUE SEAN PUBLICADOS (=1)
	datosWebPublicadoVar=datosWebLimpios[datosWebLimpios['Publicado']=='1']
	datosWebPublicadoInt=datosWebLimpios[datosWebLimpios['Publicado']==1]
	datosWebPublicado=pd.concat([datosWebPublicadoVar,datosWebPublicadoInt])

	# datosWebNoPublicado=datosWebLimpios[datosWebLimpios['Publicado']!='1']
	# print("DWL publi: ",datosWebPublicado)
	# print("DWL No publi: ",datosWebNoPublicado)

	plog(str("Publicado: "+str(len(datosWebPublicado))))
	# print(datosWebPublicado)


	
	#ORDENA LOS PRODUCTOS POR SKU
	#print("DWL: ",datosWebLimpios)
	datosWebOrdenados=datosWebPublicado.sort_values(['SKU'], axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
	#print("DWO: ",datosWebOrdenados)
	datosWeb=datosWebOrdenados
	plog(str("DWOrdenados: "+str(len(datosWeb))))
	#print(datosWeb)


	cantidadWeb=len(datosWeb)
	#print("CW: ",cantidadWeb)
	cantidadTango=len(consultaTango)-1 #SE LE RESTA UNO PORQUE CUENTA EL ENCABEZADO
	if cantidadWeb!=cantidadTango:
		plog("Cantidad Web:"+str(cantidadWeb))
		plog("Cantidad Tango:"+str(cantidadTango))

	listaSku=[]
	listaCod=[]
	cont=0

	for i in range(0,cantidadTango):
		listaCod.append(consultaTango[(i+1)][1])
	for i in range(0,cantidadWeb):
		listaSku.append(datosWeb.iloc[i][0])


	contadorOk=0
	contadorMal=0

	#LISTA DE PRECIOS UNITARIOS 
	skuUni=['011500000000010','011500000000020','011500000000040','011500000000050','011500000000060','011500000000070','011500000000090','011500000000100','011500000000110','011500000000140','011500000000150','011500000000170','011500000000180','091000000000010','011500000000130','001000000000010','001000000000020','001000000000030','011500000000060','011500000000070','011500000000110','072100000000010','072100000000020','072100000000030','072200000000010','072200000000020','072200000000030','072300000000010','072300000000020','072300000000030','019600000000040','023600000000050','023600000000010','023300000000050','023300000000041']

	#['011500000000010','011500000000020','011500000000040','011500000000050','011500000000060','011500000000070','011500000000090','011500000000100','011500000000110','011500000000130','011500000000140','011500000000150','011500000000170','011500000000180']

	# print("Datos WEB: ")
	# for i in range(len(datosWeb)):
	# 	print(datosWeb.iloc[i][0])
	# print("Datos TANGO: ")
	# for i in range(1,len(consultaTango)):
	# 	print(consultaTango[i][1])



	for i in range(cantidadWeb):
		sku=datosWeb.iloc[i][0]				#ERROR
	for i in range(cantidadTango):
		cod=consultaTango[(i+1)][1]

	cantidadMax=0
	cantidadMin=0
	if cantidadWeb>cantidadTango:
		cantidadMax=cantidadWeb
		cantidadMin=cantidadTango
	else: 
		cantidadMax=cantidadTango
		cantidadMin=cantidadWeb

	plog(str("Cantidad Maxima: "+str(cantidadMax)))
	plog(str("Cantidad Minima: "+str(cantidadMin)))



	diferencias=[]
	for i in range(cantidadMax):
		sku=datosWeb.iloc[i][0]	
		cod=consultaTango[(i+1)][1]
		if sku==cod:
			if sku in skuUni:
				precioWeb=str(f'{datosWeb.iloc[i][2]:.2f}')
				precioTango=str(f'{consultaTango[(i+1)][3]:.2f}')	
			else: 				
				precioWeb=str(f'{datosWeb.iloc[i][2]:.2f}')  #round(datosWeb.iloc[i][1],2))	
				precioTango=str(f'{consultaTango[(i+1)][2]:.2f}')
			if precioWeb==precioTango:
				contadorOk+=1
				#print("{}: SKU {} OK.".format(i,sku))
				#print("{}: productoWeb {}: {} - productoTango {}: {} - OK".format(i,sku,precioWeb,cod,precioTango))
			else: 
				contadorMal+=1
				#print(sku)#,precioWeb,precioTango)
				#print("{}: productoWeb {}: {} - productoTango {}: {}".format(i,sku,precioWeb,cod,precioTango))
				plog(str(i)+": productoWeb "+str(sku)+": "+str(precioWeb)+" - productoTango "+str(cod)+": "+str(precioTango))
		else: 
			plog("El codigo de producto de Tango es distinto al codigo de producto Web.")
			plog("SKU: "+str(sku)+" - COD: "+str(cod))

	if contadorOk+contadorMal==cantidadMax:
		plog("Cantidad de precios OK: "+str(contadorOk))
		plog("Cantidad de precios MAL: "+str(contadorMal))
	else: 
		plog("Contadores mal.")
		if cantidadTango>cantidadWeb:
			plog("Cantidad Web: "+str(cantidadWeb)+" - Cantidad Tango: "+str(cantidadTango))
			for item in listaCod:
				if item not in listaSku:
					diferencias.append(item)
			plog("####################################################################################################################################################################################")
			plog("Diferencias Tango que no están en Web: "+str(diferencias))
			plog("####################################################################################################################################################################################")
		elif cantidadWeb>cantidadTango:
			plog("Cantidad Web 2: "+str(cantidadWeb)+" - Cantidad Tango: "+str(cantidadTango))
			for item in listaSku:
				if item not in listaCod:
					print(item)
					diferencias.append(item)
			plog("####################################################################################################################################################################################")
			plog("Diferencias Web que no están en Tango: "+str(diferencias))
			plog("####################################################################################################################################################################################")
		elif cantidadWeb==cantidadTango: print("Contadores iguales.")
		else: print("Otro error, analizar.") 


################################################################################################################################
#EJECUCIÓN
################################################################################################################################

try: 
	horaInicio=dt.datetime.now()
	logErrores('C:/Users/gpereyra/Documents/GPereyra/ProgramasPython/WC-ControlPreciosTangoVsWeb/Log/CPTW_')
	plog("Log de errores creado correctamente")
except:
	print("Error al crear log de errores")
	print("ALARMA CORREO GP")

if __name__ == '__main__':
	main()
	horaFin=dt.datetime.now()
	duracion=str(horaFin-horaInicio)
	plog(f'Duración: '+duracion)
else: 
	plog("Falló ejecución: __name__!='__main__'")
	plog("ALARMA DE CORREO GP")



