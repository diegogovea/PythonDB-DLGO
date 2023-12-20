#Autor: Diego Leon Govea Ortiz
#Repositorio: PythonBD-DLGO
#Programa 1: Conexion

######################################################################
#Este programa establece conexion con el host, y muestra
#todas las bases de datos que se encuentran almacenadas
import mysql.connector

conexion = mysql.connector.connect(host="localhost", user="root", passwd="")
cursor1 = conexion.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion.close()
