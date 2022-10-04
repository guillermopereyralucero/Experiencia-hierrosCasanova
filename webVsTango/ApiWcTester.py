##############################################################################################################################################################
#LIBRERIAS
##############################################################################################################################################################
from woocommerce import API
import json
import math

##############################################################################################################################################################
#CONEXION API
##############################################################################################################################################################
"""
Las credenciales para la API de WooCommerce se gestionan en: WooCommerce --> Avanzado --> API REST

#keyMartin: ck_f6c766888884ef3b27ec4bb57b520814650167b3
#secretMartin: cs_3cd6e59e6e5e3dc05c30608b68d4a475c2493e68
"""

#FUENTE: https://woocommerce.github.io/woocommerce-rest-api-docs/?python#introduction

wcApi=API(
url="https://hierroscasanova.com.ar/",
consumer_key="ck_fa4fb9e482416eefa1a52a79e30ffe4db7bad78d",
consumer_secret="cs_7ad02575912819b22fe7fac571eb261a4adb3c99",
version="wc/v3"
)

##############################################################################################################################################################
#OBTENCION DESDE WC FAMILIAS Y VARIACIONES
##############################################################################################################################################################


idFamilia=[]
idVariaciones=[]
idFamiliasYVariaciones={}
pp=80 #DEFINO CANTIDAD DE OBJETOS POR HOJA - SE USA LUEGO EN VARIACIONES

#PARA OBTENER ID DE FAMILIAS Y ID DE VARIACIONES:
for h in range(1,10): #Al dia 220923 hay 49 familias publicadas, Si se modifican cambiar el 49 por la cantidad de familias que figuren en WC
	productos=wcApi.get("products", params={"per_page":1, "page":h, "orderby":"id"}).json()
	print(productos)
	idFamilia.append(productos[0]["id"])
	idVariaciones.append(productos[0]["variations"])
	idFamiliasYVariaciones[productos[0]["id"]]=productos[0]["variations"]
#print(idFamiliasYVariaciones)
#print(productos)
	for idProd in idFamiliasYVariaciones.keys():
		hojas=math.ceil(len(idFamiliasYVariaciones.values())/pp) #REDONDEO A HOJA SUPERIOR PARA QUE CONTENGA TODAS LAS VARIACIONES
		variaciones=wcApi.get(str("products/"+str(idProd)+"/variations"), params={"per_page": pp, "page":h, "orderby":"id"}).json()
		#var=json.dumps(variaciones,indent=2) #SI QUIERO VER EN FORMATO VISUAL/JSON
		for v in range(len(variaciones)):
			print(v)
			print(variaciones[v]["id"],variaciones[v]["sku"],variaciones[v]["regular_price"],variaciones[v]["status"],variaciones[v]["tax_status"],variaciones[v]["tax_class"])
			




###TANgo

"""

idFamilia=[26990, 26174, 25935, 25220, 22226, 18246, 7049, 6500, 6475, 6474, 6467, 6466, 6465, 6464, 6463, 6462, 6461, 6460, 6459, 6457, 6456, 6455, 6454, 6453, 6452, 6451, 6450, 6449, 6448, 6447, 6446, 6444, 6443, 6442, 6441, 6440, 6439, 6438, 6437, 6436, 6435, 6433, 6432, 6431, 6430, 6429, 6428, 3774]

variacionesIdLista=[]
for idf in idFamilia:
	producto=wcApi.get("products/"+str(idf), params={"per_page": 1}).json()
	variacionesIdLista.append(producto["variations"])
	cantidadVariaciones=len(variacionesIdLista[0])
	#print(cantidadVariaciones)
pp=80 #DEFINO CANTIDAD DE OBJETOS POR HOJA - SE USA LUEGO EN VARIACIONES
hojas=math.ceil(cantidadVariaciones/pp) #REDONDEO A HOJA SUPERIOR PARA QUE CONTENGA TODAS LAS VARIACIONES
print(hojas)
variacionesPorProducto={"idProducto":producto,"variaciones":cantidadVariaciones,"hojas":hojas}



final=[{}]
"""