#Autor: Diego Leon Govea Ortiz
#Repositorio: PythonBD-DLGO
#Programa 3: Insertar filas

######################################################################
import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="bd1")
cursor=conexion1.cursor()
sql="insert into articulos(descripcion, precio) values (%s,%s)"

a=int(input("Ingrese la cantidad de datos a registrar:"))
x=0
for x in range(a):
    nombre = input("El nombre del articulo:")
    precio = float(input("Ingrese el precio:"))
    cursor.execute(sql, (nombre, precio))
    x=x+1

conexion1.commit()
conexion1.close()
