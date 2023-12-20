#Autor: Diego Leon Govea Ortiz
#Repositorio: PythonBD-DLGO
#Programa 2: Conexion - tablas

######################################################################
#Este programa establece conexion con el host, y muestra
#las tablas de cierta base de datos
import mysql.connector

conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="bd1")
cursor1 = conexion.cursor()
cursor1.execute("show tables")
for base in cursor1:
    print(base)
conexion.close()
