REQUERIMIENTOS: 

DE CLIENTE:
-distribución equitativa de correos recibidos en casilla "ventas@hierroscasanova.com.ar".

PARA DESARROLLO: 
-gestión de agentes (activar o desactivar) según disponibilidad (licencia, tramite personal, permiso, etc.).  
-log de ejecución/histórico (puede ser .txt o SQL), control y métricas (se extraen de tablas de SQL).
-alarmas de fallo por correo (son parte del código Python y son configurables).

ALCANCES: 

-Python: será el motor de la apliación.
-SQL Server: será utilizado para...
  -tabla SQL "personal" (usuario, nombre, correo, fechaNac, telefono, sucursal, sector, puesto).
  -tabla SQL "calendario" (fecha, feriado, motivoFeriado, laboral, proceso1, proceso2, proceso3..., usuario1, usuario2, usuario3...).
-Outlook: será la aplicación utilizada para la gestión de correos (envío, recepción, distribución, redacción, etc.). 
