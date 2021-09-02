import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password= "",
    database = "pythondb"
)


mycursor = mydb.cursor()

#CREAR BASE DE DATOS
#CREATE DATABASE <nombre_DB>
#mycursor.execute("CREATE DATABASE pythondb")

#mycursor.execute("Show Databases")

#for x in mycursor:
 #   print(x)

#CREAR TABLA
#mycursor.execute("Create table clientes (nombre varchar(255), direccion varchar(255))")
#SHOW TABLES
#mycursor.execute("show tables")

#for x in mycursor:
 #   print(x)


#INSERTAR DATOS
#sql = "Insert into clientes(nombre, direccion) values (%s,%s)"
#val = ("Wilder Emmanuel", "Guatemala, Guatemala")

#mycursor.execute(sql,val)


#mydb.commit()

#print(mycursor.rowcount, "insertados exitosamente")

#INSERTAR MULTIPLES DATOS 
'''
sql = "Insert into clientes(nombre, direccion) values (%s,%s)"
val = [
    ('Nombre1','Direccion 1'),
    ('Nombre2','Direccion 2'),
    ('Nombre3','Direccion 3'),
    ('Nombre4','Direccion 4'),
    ('Nombre5','Direccion 5'),
    ('Nombre6','Direccion 6'),
    ('Nombre7','Direccion 7'),
    ('Nombre8','Direccion 8'),
    ('Nombre9','Direccion 9'),
    ('Nombre10','Direccion 10')
]

mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, " Datos insertados exitosamente")
'''

#CONSULTAR DATOS

mycursor.execute("SELECT * FROM clientes")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

