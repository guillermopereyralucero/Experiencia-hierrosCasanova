import win32com.client as client #Importa win32

#LIBRERIAS
#DEFINICIONES
#EJECUCION

"""
LOGICA: 

1.	Leer cantidad de correos.  
2.	Armar lista de agentes disponibles.
3.	Repartir 1 a 1 hasta finalizar.
4.	Guardar lo que se le envió a cada uno (o ver si queda en "enviados")
5.	Esperar y volver a empezar (con lo no enviado).

"""

outlook=client.Dispatch("Outlook.Application")	#Abre aplicacion/servicio
namespace=outlook.GetNameSpace("MAPI")	#Define espacio de trabajo
inbox=namespace.GetDefaultFolder(6)	#Bandeja de entrada por default (6) #FUENTE: https://docs.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders
cuenta=namespace.Folders["ventas@hierroscasanova.com.ar"]	#ELEGIR CUENTA (Si hay mas de una) O CARPETA GENERAL
print("Carpeta a trabajar:",cuenta.Name)
# for folder in inbox.Folders:			#PARA VER CARPETAS
# 	print(folder.Name) 
inbox=cuenta.Folders["Bandeja de entrada"] #ELEGIR CARPETA
items=inbox.Items.restrict("[ReceivedTime] > '5/01/2022 08:00 AM'")	 #SIN restrict TRAE LOS ASUNTOS, con restrict filtra. FUENTE: https://docs.microsoft.com/en-us/office/vba/api/outlook.items.restrict
cantCorreos=items.Count	#Conteo cantidad de correos #FUENTE: https://docs.microsoft.com/en-us/office/vba/api/outlook.mailitem
print("Cantidad de correos en carpeta:",cantCorreos)
correos=[]
for i in range(cantCorreos-1089):
	correos.append({"id":items[i].EntryID,"asunto":str(items[i]),"cuentaRemitente":str(items[i].SenderEmailAddress),"fechaCreacion":str(items[i].CreationTime)})
	#print("Asunto: "+str(items[i])+" - CuentaRemitente: "+str(items[i].SenderEmailAddress)+" - Fecha: "+str(items[i].CreationTime)+" - ID: "+str(items[i].EntryID))
	print(items[0])
	mail=items[0] #[10]
	mail.Reply()
	mail.To="gpereyra@hierroscasanova.com.ar"
	mail.CC="guillermo.pereyra.hc@gmail.com"
	#mail.Body="Respuesta de prueba 123"
	mail.Display()
	mail.Save()
	mail.Send()
print(correos)






# outlook=client.Dispatch("Outlook.Application").GetNamespace("MAPI")
# inbox=outlook.GetDefaultFolder(6) 
# mails=inbox.Items.restrict("[ReceivedTime] > '4/27/2022 08:00 AM'")		#FUENTE: https://docs.microsoft.com/en-us/office/vba/api/outlook.items.restrict
# print(mails.Count)

# for message in messages:
#     NewMsg = message.Forward()
#     NewMsg.Body = message.Body
#     NewMsg.Subject = message.Subject
#     NewMsg.To = "mail@mail.com"
#     NewMsg.Send()



# #PARA ENVIO DE MAIL: 
# mail=outlook.CreateItem(0)
# mail.SentOnBehalfOfName="ventas@hierroscasanova.com.ar"
# mail.To="gpereyra@hierroscasanova.com.ar"
# mail.CC="guillermo.pereyra.hc@gmail.com"
# mail.Subject="1,2,3 probando - Correo enviado con Python"
# mail.Body="Este correo lo envie con Python, sería el reenviador que tomaría de ventas y enviaría a cada 'agente'"
# mail.Display()
# mail.Save()
# # mail.Send()





"""
#PARA CONDICIONES FUTURAS:
for i in range(0,len(Correos)):
	if Correos[i].Sender=="vecarluccio@ferrovias.com.ar":
		print("ENCONTRADO: ",Correos[i].Sender)
"""


# mails=inbox.Items
# print(mails[1]) #Subject
# print(mails[1].Sender)
# print(mails[1].SenderEmailAddress)

#for mail in mails:
	#print(mail.Subject)
	#print(mail.Sender)


#mailsFiltrados=[item for item in mails if "" in item.Subject]

# for i in range(0,len(mails)): #len(mails)):
# 	if mails[i].Sender=="lucas argañaraz":
# 		print("ENCONTRADO",mails[i].Sender)
# 	# else: print("NO ENCONTRADO")

#print(len(mails))

#print([item for item in mails if "GT " in item.Subject])
	#print(item.Sender)

#print(len(mailsFiltrados))

# for mail in mailsFiltrados:
# 	mail.Reply()
# 	mail.To="gpereyra@hierroscasanova.com.ar"
# 	mail.Body="Respuesta de prueba 123"
# 	mail.Display()
	#mail.Send()














# #PARA ENVIO DE MAIL: 
# mail=outlook.CreateItem(0)
# mail.To="gpereyra@hierroscasanova.com.ar"
# mail.CC="guillermo.pereyra.hc@gmail.com"
# mail.Subject="1,2,3 probando - Correo enviado con Python"
# mail.Body="Agus, este correo lo envie con Python, sería el reenviador que tomaría de ventas y enviaría a cada 'agente'"
# mail.Display()
# mail.Save()
# mail.Send()


