#Autor: Diego Leon Govea Ortiz
#Repositorio: PythonBD-DLGO
#Programa 4: Consultar

######################################################################
import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="bd1")
cursor=conexion1.cursor()
cursor.execute("select codigo, descripcion, precio from articulos")
for fila in cursor:
    print(fila)
conexion1.close()
