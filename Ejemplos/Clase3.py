'''
"r"   Opens a file for reading only.
"r+"  Opens a file for both reading and writing.
"rb"  Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w"   Opens a file for writing only.
"a"   Open for writing.  The file is created if it does not exist.
'''

from os import read


archivo = open('Lectura.txt')

#Leer o imprimir el contenido del archivo
#print(archivo.readline())
#print(archivo.readline())
#print(archivo.readline())

'''
linea = archivo.readline()
while linea != "":
    print(linea)
    linea = archivo.readline()
'''

#for linea in archivo:
    #procesamos la linea
 #   print(linea)

#Cerrar el archivo
#archivo.close()
print(archivo.readlines())

'''
i = 1
for linea in archivo:
     linea = linea.rstrip("\\n")
     print(" %4d: %s" % (i, linea))
     i+=1
archivo.close

'''

#UNIX fin de linea = \n
#WINDOWS \r \n
#Mac \r

#archivo.write(cadena)
#archivo.writelines(lista_cadenas)

saludo = open("saludo.py", "w")
saludo.write("""
print("Hola Mundo") \n""")
saludo.close()

contenido = """print("NuevaLinea")"""

archivo = open("saludo.py", "a")
archivo.write(contenido)
print("Escritura de archivo exitosa")
archivo.close()

#Funciones

def get_File(ruta, permiso):
    archivo = open(ruta, permiso)
    return archivo

archivo = get_File("Lectura.txt", "r+")
print(archivo.readline())


#Cononcer la posicion actual del archivo en forma binaria
#archivo.tell()
#Para modificar la posicion actual se utiliza
# archivo.seek(inicio, desde)


