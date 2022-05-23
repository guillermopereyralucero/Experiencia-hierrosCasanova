from woocommerce import API
import json


wcApi=API(
url="https://hierroscasanova.com.ar/",
consumer_key="ck_fa4fb9e482416eefa1a52a79e30ffe4db7bad78d",
consumer_secret="cs_7ad02575912819b22fe7fac571eb261a4adb3c99",
version="wc/v3"
)

proId=[3774,6428,6429,6430,6431,6432,6433,6435,6436,6437,6438,6439,6440,6441,6442,6443,6444,6446,6447,6448,6449,6450,6451,6452,6453,6454,6455,6456,6457,6459,6460,6461,6462,6463,6464,6465,6466,6467,6474,6475,6500,7049,18246,22226,25220,25935,25980]

prod_list=[]

#productos=wcApi.get("products", params={"per_page": 1}).json() #Hasta 30 #SIN .json() devuelve <Response [200]> ////// CON .json() DEVUELVE LISTA [] DE DICCIONARIOS {}
for p in proId:
	producto=wcApi.get("products/"+str(p), params={"per_page": 1}).json()
	prod=json.dumps(producto,indent=1) # Puedo usar "products/25980" por ejemplo para buscar un unico producto por ID
	#print(prod) #PARA VISUALIZAR IDENTADO
	#print(producto["id"])
	prod_list.append([producto["id"],producto["name"],producto["variations"]])
	
print(prod_list) # LISTA [] DE DICCIONARIOS {}







# # print()
# # print(productos[9]) # DICCIONARIO {}
# proId=[]
# proName=[]
# proVar=[]

# print(productos)

# for i in range(1,len(productos)):
# 	proId.append(productos[i]["id"])
# 	proName.append(productos[i]["name"])
# 	proVar.append(productos[i]["variations"])
# 	print(i,proId[i],proName[i],proVar[i]) # MEDIANTE LA CLAVE OBTENGO VALORES

# # cont=0
# # for prod in range(len(proId)):
# # 	variaciones=wcApi.get(str("products/"+str(proId[prod])+"/variations"), params={"per_page": 100}).json() #DEVUELVE LISTA [] DE DICCIONARIOS {}
# # 	for var in range(len(variaciones)):
# # 		print(cont,proId[prod],proName[prod],variaciones[var]["id"],variaciones[var]["sku"],format(float(variaciones[var]["regular_price"]),'.2f'),variaciones[var]["status"],variaciones[var]["tax_status"],variaciones[var]["date_modified"])
# # 		cont+=1





# # # for i in range(len(variaciones)):
# # # 	print(i,variaciones[i]["id"],variaciones[i]["attributes"][2]["option"],variaciones[i]["sku"],variaciones[i]["price"])
# # # for i in variaciones: 
# # # 	print(i,variaciones[i]["id"],variaciones[i]["attributes"][2]["option"],variaciones[i]["sku"],variaciones[i]["price"])
