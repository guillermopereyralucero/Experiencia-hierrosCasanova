from woocommerce import API

wcApi=API(
url="https://hierroscasanova.com.ar/",
consumer_key="ck_f6c766888884ef3b27ec4bb57b520814650167b3",
consumer_secret="cs_3cd6e59e6e5e3dc05c30608b68d4a475c2493e68",
version="wc/v3"
)

productos=wcApi.get("products", params={"per_page": 100}).json() #SIN .json() devuelve <Response [200]> ////// CON .json() DEVUELVE LISTA [] DE DICCIONARIOS {}
#print(productos) # LISTA [] DE DICCIONARIOS {}
# print()
# print(productos[9]) # DICCIONARIO {}
# print()
#variaciones=
proId=[]
proName=[]
proVar=[]

for i in range(len(productos)-40):
	proId.append(productos[i]["id"])
	proName.append(productos[i]["name"])
	proVar.append(productos[i]["variations"])
	#print(i,proId[i],proName[i],proVar[i]) # MEDIANTE LA CLAVE OBTENGO VALORES

cont=0
for prod in range(len(proId)):
	variaciones=wcApi.get(str("products/"+str(proId[prod])+"/variations"), params={"per_page": 100}).json() #DEVUELVE LISTA [] DE DICCIONARIOS {}
	for var in range(len(variaciones)):
		print(cont,proId[prod],proName[prod],variaciones[var]["id"],variaciones[var]["sku"],format(float(variaciones[var]["regular_price"]),'.2f'),variaciones[var]["status"],variaciones[var]["tax_status"],variaciones[var]["date_modified"])
		cont+=1





# for i in range(len(variaciones)):
# 	print(i,variaciones[i]["id"],variaciones[i]["attributes"][2]["option"],variaciones[i]["sku"],variaciones[i]["price"])
# for i in variaciones: 
# 	print(i,variaciones[i]["id"],variaciones[i]["attributes"][2]["option"],variaciones[i]["sku"],variaciones[i]["price"])
