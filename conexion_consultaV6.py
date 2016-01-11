#!/usr/bin/python
# -*- coding: latin-1 -*-

import MySQLdb
# Variable con la configuracion de la conexion
db= MySQLdb.Connect('localhost', 'root', '1234', 'kf_json')
# conectamos al servidor MySql
cursor = db.cursor()

#CONSULTA CON MAS DE 2 CARACTERISTICAS
#result = cursor.execute("SELECT * FROM data_capturev4 WHERE Happy='Yes' AND Engage='Yes' AND WearingGlasses='yes' AND LeftEyeClosed='yes'")

#CONSULTA CON NORMAL DOS CARACTERISTICAS
result = cursor.execute("SELECT * FROM data_capturev4 WHERE Happy='Yes' AND Engage='Yes'")
rows = cursor.fetchall()

print '\nPOSICIONES Y ULTIMA CONSULTA ENCONTRDA\n'
for lista in rows:
    print (lista)

print '\nIMPRIME EN UN RENGLON LOS DATOS COMPLETOS'
#print rows
print 'Cantidad de elementos encontrados: %s' % (result)

#ELEMENTOS DE LA BASE DE DATOS
#for rows in cursor.fetchall():
#    print rows

# Cerramos la variable encargada de las consultas
cursor.close()
# Cerramos la conexión
db.close()