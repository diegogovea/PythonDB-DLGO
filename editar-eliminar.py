#Autor: TutorialesProgramacionYYA
#Repositorio: PythonBD-DLGO
#Programa 5: Eliminar - Modificar

######################################################################
import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="bd1")
cursor1=conexion1.cursor()
cursor1.execute("delete from articulos where codigo=5")
cursor1.execute("update articulos set precio=50 where codigo=7")
conexion1.commit()
cursor1.execute("select codigo, descripcion, precio from articulos")
for fila in cursor1:
    print(fila)
conexion1.close()
