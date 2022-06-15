from woocommerce import API
import json

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

proId=[6448]#,3774,6428,6429,6430,6431,6432,6433,6435,6436,6437,6438,6439,6440,6441,6442,6443,6444,6446,6447,6448,6449,6450,6451,6452,6453,6454,6455,6456,6457,6459,6460,6461,6462,6463,6464,6465,6466,6467,6474,6475,6500,7049,18246,22226,25220,25935,25980]

prod_list=[]
variacionesIdLista=[]

#productos=wcApi.get("products", params={"per_page": 1}).json() #Hasta 30 #SIN .json() devuelve <Response [200]> ////// CON .json() DEVUELVE LISTA [] DE DICCIONARIOS {}

"""
for p in proId:
	producto=wcApi.get("products/"+str(p), params={"per_page": 1}).json()
	#print(producto)
	prod=json.dumps(producto,indent=1) # Puedo usar "products/25980" por ejemplo para buscar un unico producto por ID
	#print(prod) #PARA VISUALIZAR IDENTADO
	#print(producto["id"])
	prod_list.append([producto["id"],producto["name"],producto["variations"]])
	variacionesIdLista.append(producto["variations"])
#print(prod_list) # LISTA [] DE DICCIONARIOS {}
"""

variaciones=wcApi.get("products/6448/variations", params={"per_page": 80, "page":1}).json()
var=json.dumps(variaciones,indent=2)
#print(var)
#print(variaciones[0][0]["id"],variaciones[0][0]["sku"],variaciones[0][0]["regular_price"],variaciones[0][0]["status"],variaciones[0][0]["tax_status"],variaciones[0][0]["tax_class"])

#print(variaciones["id"],variaciones["sku"],variaciones["regular_price"],variaciones["status"],variaciones["tax_status"],variaciones["tax_class"])
print(variaciones[0]["id"],variaciones[0]["sku"],variaciones[0]["regular_price"],variaciones[0]["status"],variaciones[0]["tax_status"],variaciones[0]["tax_class"])


print(len(variaciones))
for v in range(len(variaciones)):
	print(v)
	print(variaciones[v]["id"],variaciones[v]["sku"],variaciones[v]["regular_price"],variaciones[v]["status"],variaciones[v]["tax_status"],variaciones[v]["tax_class"])


variaciones=wcApi.get("products/6448/variations", params={"per_page": 80, "page":2}).json()
var=json.dumps(variaciones,indent=2)
#print(var)
#print(variaciones[0][0]["id"],variaciones[0][0]["sku"],variaciones[0][0]["regular_price"],variaciones[0][0]["status"],variaciones[0][0]["tax_status"],variaciones[0][0]["tax_class"])

#print(variaciones["id"],variaciones["sku"],variaciones["regular_price"],variaciones["status"],variaciones["tax_status"],variaciones["tax_class"])
print(variaciones[0]["id"],variaciones[0]["sku"],variaciones[0]["regular_price"],variaciones[0]["status"],variaciones[0]["tax_status"],variaciones[0]["tax_class"])


print(len(variaciones))
for v in range(len(variaciones)):
	print(v)
	print(variaciones[v]["id"],variaciones[v]["sku"],variaciones[v]["regular_price"],variaciones[v]["status"],variaciones[v]["tax_status"],variaciones[v]["tax_class"])
